"""Small JSON schema validator for Stage 3.1 synthetic artifacts.

This intentionally implements only the JSON Schema subset used by this project.
It avoids adding dependencies while still catching required fields, type errors,
enum/const violations, object shape mistakes and the conditional metric-artifact
rules introduced in Stage 3.0.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


class SchemaValidationError(ValueError):
    """Raised when an artifact does not satisfy the expected schema."""


def load_json(path: str | Path) -> Any:
    with Path(path).open("r", encoding="utf-8") as f:
        return json.load(f)


def validate_file(schema_path: str | Path, json_path: str | Path) -> None:
    validate(load_json(json_path), load_json(schema_path), path="$")


def validate(instance: Any, schema: dict[str, Any], path: str = "$") -> None:
    if "if" in schema and _matches(instance, schema["if"]):
        validate(instance, schema.get("then", {}), path)

    for sub_schema in schema.get("allOf", []):
        validate(instance, sub_schema, path)

    if "oneOf" in schema:
        errors: list[str] = []
        ok = 0
        for candidate in schema["oneOf"]:
            try:
                validate(instance, candidate, path)
            except SchemaValidationError as exc:
                errors.append(str(exc))
            else:
                ok += 1
        if ok != 1:
            raise SchemaValidationError(
                f"{path}: expected exactly one oneOf match, got {ok}; errors={errors}"
            )

    if "const" in schema and instance != schema["const"]:
        raise SchemaValidationError(f"{path}: expected const {schema['const']!r}, got {instance!r}")

    if "enum" in schema and instance not in schema["enum"]:
        raise SchemaValidationError(f"{path}: expected one of {schema['enum']!r}, got {instance!r}")

    if "type" in schema:
        _validate_type(instance, schema["type"], path)

    if isinstance(instance, dict):
        _validate_object(instance, schema, path)
    elif isinstance(instance, list):
        _validate_array(instance, schema, path)
    elif isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            raise SchemaValidationError(f"{path}: expected >= {schema['minimum']}, got {instance}")


def _validate_type(instance: Any, expected: str | list[str], path: str) -> None:
    expected_types = [expected] if isinstance(expected, str) else expected
    if any(_is_type(instance, t) for t in expected_types):
        return
    raise SchemaValidationError(f"{path}: expected type {expected_types!r}, got {type(instance).__name__}")


def _is_type(instance: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(instance, dict)
    if expected == "array":
        return isinstance(instance, list)
    if expected == "string":
        return isinstance(instance, str)
    if expected == "integer":
        return isinstance(instance, int) and not isinstance(instance, bool)
    if expected == "number":
        return isinstance(instance, (int, float)) and not isinstance(instance, bool)
    if expected == "boolean":
        return isinstance(instance, bool)
    if expected == "null":
        return instance is None
    raise SchemaValidationError(f"$schema: unsupported schema type {expected!r}")


def _validate_object(instance: dict[str, Any], schema: dict[str, Any], path: str) -> None:
    for key in schema.get("required", []):
        if key not in instance:
            raise SchemaValidationError(f"{path}: missing required field {key!r}")

    properties = schema.get("properties", {})
    if schema.get("additionalProperties") is False:
        extras = sorted(set(instance) - set(properties))
        if extras:
            raise SchemaValidationError(f"{path}: unexpected fields {extras!r}")

    for key, value in instance.items():
        if key in properties:
            validate(value, properties[key], f"{path}.{key}")
        elif isinstance(schema.get("additionalProperties"), dict):
            validate(value, schema["additionalProperties"], f"{path}.{key}")


def _validate_array(instance: list[Any], schema: dict[str, Any], path: str) -> None:
    if schema.get("uniqueItems") and len(instance) != len(set(instance)):
        raise SchemaValidationError(f"{path}: duplicate array items are not allowed")
    if "items" in schema:
        for idx, value in enumerate(instance):
            validate(value, schema["items"], f"{path}[{idx}]")


def _matches(instance: Any, condition: dict[str, Any]) -> bool:
    try:
        validate(instance, condition, "$")
    except SchemaValidationError:
        return False
    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate a JSON artifact against a project schema.")
    parser.add_argument("--schema", required=True, help="Path to a JSON schema file.")
    parser.add_argument("--json", required=True, help="Path to a JSON artifact file.")
    args = parser.parse_args(argv)
    validate_file(args.schema, args.json)
    print(f"validated: {args.json} against {args.schema}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
