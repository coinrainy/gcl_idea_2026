"""Method interface placeholders for Stage 3.1."""

from __future__ import annotations

from dataclasses import dataclass


SCAFFOLD_ERROR = "Stage 3.1 scaffold only; real training is not implemented."


@dataclass(frozen=True)
class MethodSpec:
    method_name: str
    objective_family: str
    requires_decoder: bool
    uses_negatives: bool
    uses_target_encoder: bool
    default_config_path: str


class Stage31MethodPlaceholder:
    spec: MethodSpec

    @property
    def method_name(self) -> str:
        return self.spec.method_name

    @property
    def objective_family(self) -> str:
        return self.spec.objective_family

    @property
    def requires_decoder(self) -> bool:
        return self.spec.requires_decoder

    @property
    def uses_negatives(self) -> bool:
        return self.spec.uses_negatives

    @property
    def uses_target_encoder(self) -> bool:
        return self.spec.uses_target_encoder

    @property
    def default_config_path(self) -> str:
        return self.spec.default_config_path

    def build_model(self) -> None:
        raise NotImplementedError(SCAFFOLD_ERROR)

    def pretrain(self) -> None:
        raise NotImplementedError(SCAFFOLD_ERROR)

    def encode(self) -> None:
        raise NotImplementedError(SCAFFOLD_ERROR)
