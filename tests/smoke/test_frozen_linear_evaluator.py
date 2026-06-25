from gcl_diag.eval.frozen_linear import FrozenLinearEvaluator


def test_frozen_linear_dry_run() -> None:
    embeddings = [
        [0.0, 0.0],
        [0.1, 0.0],
        [1.0, 1.0],
        [1.1, 1.0],
        [0.0, 0.2],
        [1.2, 0.9],
        [0.2, 0.1],
        [1.0, 0.8],
        [0.1, 0.2],
        [1.1, 1.1],
        [0.2, 0.0],
        [1.2, 1.0],
    ]
    labels = [0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    result = FrozenLinearEvaluator(evaluator_seed=0, max_epochs=5, patience=2).evaluate(
        embeddings,
        labels,
        train_indices=[0, 1, 2, 3],
        val_indices=[4, 5, 6, 7],
        test_indices=[8, 9, 10, 11],
    )
    assert result.best_epoch == 3
    assert 0.0 <= result.valid_at_best <= 1.0
    assert 0.0 <= result.test_at_best <= 1.0
