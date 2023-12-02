import pytest
from app import get_possible_game, get_min_cubes


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Game 59: 4 red, 4 green; 5 blue, 1 green, 20 red; 11 red, 3 green, 15 blue; 5 blue, 7 red, 3 green; 18 blue, 4 green, 19 red", None),
        ("Game 64: 4 green, 7 blue, 10 red; 3 green, 4 blue, 12 red; 6 green, 6 red, 8 blue; 4 green, 9 red, 1 blue; 2 blue, 15 red, 15 green", None),
        ("Game 80: 3 green, 5 red, 9 blue; 3 red, 5 blue, 2 green; 5 green, 6 red, 2 blue", 80),
        ("Game 82: 4 green, 8 blue, 7 red; 10 blue, 1 green, 10 red; 7 blue, 4 green, 5 red", 82)
    ],
)
def test_get_possible_game(text, expected):
    assert get_possible_game(text) == expected

@pytest.mark.parametrize(
    "text, expected",
    [
        ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", [4,2,6]),
        ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", [1,3,4]),
        ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", [20,13,6]),
        ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", [14,3,15]),
        ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", [6,3,2])
    ],
)
def test_get_min_cubes(text, expected):
    assert get_min_cubes(text) == expected
