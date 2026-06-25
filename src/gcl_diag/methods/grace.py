"""GRACE placeholder."""

from __future__ import annotations

from .base import MethodSpec, Stage31MethodPlaceholder


class GRACEPlaceholder(Stage31MethodPlaceholder):
    spec = MethodSpec(
        method_name="GRACE",
        objective_family="negative_based_contrastive",
        requires_decoder=False,
        uses_negatives=True,
        uses_target_encoder=False,
        default_config_path="configs/methods/grace.yaml",
    )
