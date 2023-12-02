import pytest
from app2 import get_first_and_last


@pytest.mark.parametrize(
    "text, expected",
    [
        ("tpxrcthqbktwoeightonepcc4tzf26", 26),
        ("659nfbpb", 69),
        ("oneone2", 12),
        ("tmppzkhk49nine4", 44),
        ("nineight", 98),
        ("one", 11),
        ("threeeightfive6fxlckcsskpnd", 36),
    ],
)
def test_get_first_and_last(text, expected):
    assert get_first_and_last(text) == expected