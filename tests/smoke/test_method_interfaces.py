import pytest

from gcl_diag.methods import BGRLPlaceholder, GRACEPlaceholder, GraphMAEPlaceholder


@pytest.mark.parametrize(
    "method_cls,expected_name",
    [
        (GRACEPlaceholder, "GRACE"),
        (BGRLPlaceholder, "BGRL"),
        (GraphMAEPlaceholder, "GraphMAE"),
    ],
)
def test_method_placeholders_block_training(method_cls, expected_name: str) -> None:
    method = method_cls()
    assert method.method_name == expected_name
    with pytest.raises(NotImplementedError, match="Stage 3.1 scaffold only"):
        method.pretrain()
