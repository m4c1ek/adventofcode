import pytest
from app import get_part_numbers


@pytest.mark.parametrize(
    "text, expected",
    [
        (
            [
                "467..114..",
                "...*......",
                "..35..633.",
                "......#...",
                "617*......",
                ".....+.58.",
                "..592.....",
                "......755.",
                "...$.*....",
                ".664.598..",
            ],
            ['467', '35', '633', '617', '592', '755', '664', '598'],
        ),
    ],
)
def test_get_part_numbers(text, expected):
    assert get_part_numbers(text) == expected
