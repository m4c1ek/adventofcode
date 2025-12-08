import pytest
from main import count_where_adjacent_at_symbols_less_equal


def test_count_where_adjacent_at_symbols_less_equal_n3():
    """Test case: grid with @ symbols, counting positions where adjacent @ symbols <= 3"""
    grid_input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

    result = count_where_adjacent_at_symbols_less_equal(grid_input, n=3)
    assert result == 13


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
