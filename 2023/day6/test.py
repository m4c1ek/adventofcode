import pytest
from app import get_wins_num

@pytest.mark.parametrize(
    "time_and_distance, wins_number",
    [
        ([7,9], 4),
        ([15,40], 8),
        ([30,200], 9),
    ],
)
def test_get_wins(time_and_distance, wins_number):
    assert get_wins_num(time_and_distance[0], time_and_distance[1]) == wins_number 