import pytest
from main import move


class TestMove:
    """Test the move() function with examples from Advent of Code assignment."""

    def test_full_sequence(self):
        """
        Test the complete sequence from the problem description.
        Expected: 6 total times pointing at 0 (3 during rotation + 3 at end).
        """
        rotations = [
            # (direction, steps, expected_final_position, expected_zero_count, description)
            (-1, 68, 82, 1, "L68: points at 0 once during rotation"),
            (-1, 30, 52, 0, "L30: no zeros"),
            (1, 48, 0, 1, "R48: points at 0 (end of rotation)"),
            (-1, 5, 95, 1, "L5: no zeros during rotation"),
            (1, 60, 55, 1, "R60: points at 0 once during rotation"),
            (-1, 55, 0, 0, "L55: points at 0 (end of rotation)"),
            (-1, 1, 99, 1, "L1: no zeros"),
            (-1, 99, 0, 0, "L99: points at 0 (end of rotation)"),
            (1, 14, 14, 0, "R14: no zeros"),
            (-1, 82, 32, 1, "L82: points at 0 once during rotation"),
        ]

        current_position = 50
        total_zeros = 0

        for direction, steps, expected_pos, expected_zeros, description in rotations:
            final_pos, zero_count = move(current_position, direction, steps)

            assert final_pos == expected_pos, (
                f"{description}: Expected final position {expected_pos}, got {final_pos}"
            )

            total_zeros += zero_count
            current_position = final_pos

        assert total_zeros == 6, f"Expected total of 6 zeros, got {total_zeros}"

    def test_l68_from_50(self):
        """L68 from 50 → 82, points at 0 once during rotation."""
        final_pos, zero_count = move(50, -1, 68)
        assert final_pos == 82
        assert zero_count == 1

    def test_l30_from_82(self):
        """L30 from 82 → 52, no zeros."""
        final_pos, zero_count = move(82, -1, 30)
        assert final_pos == 52
        assert zero_count == 0

    def test_r48_from_52(self):
        """R48 from 52 → 0, points at 0."""
        final_pos, zero_count = move(52, 1, 48)
        assert final_pos == 0
        assert zero_count == 1

    def test_l5_from_0(self):
        """L5 from 0 → 95."""
        final_pos, zero_count = move(0, -1, 5)
        assert final_pos == 95
        assert zero_count == 0

    def test_r60_from_95(self):
        """R60 from 95 → 55, points at 0 once during rotation."""
        final_pos, zero_count = move(95, 1, 60)
        assert final_pos == 55
        assert zero_count == 1

    def test_l55_from_55(self):
        """L55 from 55 → 0, points at 0."""
        final_pos, zero_count = move(55, -1, 55)
        assert final_pos == 0
        assert zero_count == 1

    def test_l1_from_0(self):
        """L1 from 0 → 99."""
        final_pos, zero_count = move(0, -1, 1)
        assert final_pos == 99
        assert zero_count == 0

    def test_l99_from_99(self):
        """L99 from 99 → 0, points at 0."""
        final_pos, zero_count = move(99, -1, 99)
        assert final_pos == 0
        assert zero_count == 1

    def test_r14_from_0(self):
        """R14 from 0 → 14, no zeros."""
        final_pos, zero_count = move(0, 1, 14)
        assert final_pos == 14
        assert zero_count == 0

    def test_l82_from_14(self):
        """L82 from 14 → 32, points at 0 once during rotation."""
        final_pos, zero_count = move(14, -1, 82)
        assert final_pos == 32
        assert zero_count == 1

    def test_r1000_from_50(self):
        """
        Edge case from problem: R1000 from 50 causes dial to point at 0 ten times.
        "if the dial were pointing at 50, a single rotation like R1000 would cause
        the dial to point at 0 ten times before returning back to 50!"
        """
        final_pos, zero_count = move(50, 1, 1000)
        assert final_pos == 50  # Returns to starting position (1050 % 100 = 50)
        assert zero_count == 10  # Points at 0 ten times (at 100, 200, ..., 1000)
