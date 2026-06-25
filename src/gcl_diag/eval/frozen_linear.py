"""Synthetic-only frozen linear evaluator dry-run scaffold."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class FrozenLinearResult:
    best_epoch: int
    valid_at_best: float
    test_at_best: float
    final_valid: float
    final_test: float


class FrozenLinearEvaluator:
    """A deterministic nearest-centroid dry-run with a frozen-evaluator shape.

    This is not a real GCL evaluator. It exists only to exercise Stage 3.1
    interfaces on synthetic embeddings without touching datasets or GPUs.
    """

    def __init__(
        self,
        evaluator_seed: int = 0,
        early_stopping_metric: str = "validation_accuracy",
        max_epochs: int = 5,
        patience: int = 2,
    ) -> None:
        self.evaluator_seed = evaluator_seed
        self.early_stopping_metric = early_stopping_metric
        self.max_epochs = max_epochs
        self.patience = patience

    def evaluate(
        self,
        embeddings: Sequence[Sequence[float]],
        labels: Sequence[int],
        train_indices: Sequence[int],
        val_indices: Sequence[int],
        test_indices: Sequence[int],
    ) -> FrozenLinearResult:
        if self.early_stopping_metric != "validation_accuracy":
            raise ValueError("Stage 3.1 dry-run only supports validation_accuracy")
        _validate_inputs(embeddings, labels, train_indices, val_indices, test_indices)
        centroids = _centroids(embeddings, labels, train_indices)
        predictions = [_predict(row, centroids) for row in embeddings]
        valid_acc = _accuracy(predictions, labels, val_indices)
        test_acc = _accuracy(predictions, labels, test_indices)
        best_epoch = min(max(self.patience + 1, 1), self.max_epochs)
        return FrozenLinearResult(
            best_epoch=best_epoch,
            valid_at_best=valid_acc,
            test_at_best=test_acc,
            final_valid=valid_acc,
            final_test=test_acc,
        )


def _validate_inputs(
    embeddings: Sequence[Sequence[float]],
    labels: Sequence[int],
    train_indices: Sequence[int],
    val_indices: Sequence[int],
    test_indices: Sequence[int],
) -> None:
    if len(embeddings) != len(labels):
        raise ValueError("embeddings and labels must have the same length")
    if not train_indices or not val_indices or not test_indices:
        raise ValueError("train/val/test indices must be non-empty")
    for idx in list(train_indices) + list(val_indices) + list(test_indices):
        if idx < 0 or idx >= len(labels):
            raise ValueError("index out of range")


def _centroids(embeddings: Sequence[Sequence[float]], labels: Sequence[int], train_indices: Sequence[int]) -> dict[int, list[float]]:
    sums: dict[int, list[float]] = {}
    counts: dict[int, int] = {}
    for idx in train_indices:
        label = labels[idx]
        row = [float(x) for x in embeddings[idx]]
        sums.setdefault(label, [0.0] * len(row))
        counts[label] = counts.get(label, 0) + 1
        for j, value in enumerate(row):
            sums[label][j] += value
    return {label: [value / counts[label] for value in values] for label, values in sums.items()}


def _predict(row: Sequence[float], centroids: dict[int, list[float]]) -> int:
    best_label = None
    best_dist = None
    for label, centroid in centroids.items():
        dist = sum((float(a) - b) ** 2 for a, b in zip(row, centroid))
        if best_dist is None or dist < best_dist:
            best_label = label
            best_dist = dist
    if best_label is None:
        raise ValueError("no centroids available")
    return best_label


def _accuracy(predictions: Sequence[int], labels: Sequence[int], indices: Sequence[int]) -> float:
    correct = sum(1 for idx in indices if predictions[idx] == labels[idx])
    return correct / len(indices)
