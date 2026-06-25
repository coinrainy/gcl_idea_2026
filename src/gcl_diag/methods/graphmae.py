"""GraphMAE placeholder."""

from __future__ import annotations

from .base import MethodSpec, Stage31MethodPlaceholder


class GraphMAEPlaceholder(Stage31MethodPlaceholder):
    spec = MethodSpec(
        method_name="GraphMAE",
        objective_family="masked_graph_modeling",
        requires_decoder=True,
        uses_negatives=False,
        uses_target_encoder=False,
        default_config_path="configs/methods/graphmae.yaml",
    )
