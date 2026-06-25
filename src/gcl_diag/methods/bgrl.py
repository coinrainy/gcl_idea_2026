"""BGRL placeholder."""

from __future__ import annotations

from .base import MethodSpec, Stage31MethodPlaceholder


class BGRLPlaceholder(Stage31MethodPlaceholder):
    spec = MethodSpec(
        method_name="BGRL",
        objective_family="bootstrap_negative_free",
        requires_decoder=False,
        uses_negatives=False,
        uses_target_encoder=True,
        default_config_path="configs/methods/bgrl.yaml",
    )
