import pytest
from main import is_valid_id


class TestIsValidId:
    """Test suite for is_valid_id method based on Advent of Code guidelines."""

    # Invalid IDs - these should return False
    @pytest.mark.parametrize(
        "invalid_id",
        [
            # Single digit repeated twice
            11,
            22,
            55,
            99,
            # Two digits repeated twice
            6464,
            1010,
            # Three digits repeated twice
            123123,
            # From AoC examples
            1188511885,  # From range 1188511880-1188511890
            222222,  # From range 222220-222224 (single digit repeated 6 times)
            446446,  # From range 446443-446449
            38593859,  # From range 38593856-38593862
        ],
    )
    def test_invalid_ids_return_false(self, invalid_id):
        """Test that IDs with patterns repeated twice (or more) are invalid."""
        assert is_valid_id(invalid_id) is False, f"{invalid_id} should be invalid"

    # Valid IDs - these should return True
    @pytest.mark.parametrize(
        "valid_id",
        [
            # Single digits
            0,
            1,
            5,
            9,
            # From AoC examples - boundaries of ranges with invalid IDs
            95,
            115,
            998,
            1012,
            1188511880,
            1188511890,
            222220,
            222224,
            # From ranges with no invalid IDs
            1698522,
            1698523,
            1698524,
            1698525,
            1698526,
            1698527,
            1698528,
            446443,
            446444,
            446445,
            446447,
            446448,
            446449,
            38593856,
            38593857,
            38593858,
            38593860,
            38593861,
            38593862,
            # Other valid numbers
            101,  # Mentioned in problem (not 0101 with leading zero)
            12,
            123,
            1234,
            98,
        ],
    )
    def test_valid_ids_return_true(self, valid_id):
        """Test that IDs without repeated patterns are valid."""
        assert is_valid_id(valid_id) is True, f"{valid_id} should be valid"

    def test_range_11_to_22_has_two_invalid(self):
        """Test example: 11-22 has two invalid IDs, 11 and 22."""
        invalid_count = sum(1 for i in range(11, 23) if not is_valid_id(i))
        assert invalid_count == 2
        assert not is_valid_id(11)
        assert not is_valid_id(22)

    def test_range_95_to_115_has_two_invalid(self):
        """Test example: 95-115 has two invalid IDs, 99 and 111."""
        invalid_count = sum(1 for i in range(95, 116) if not is_valid_id(i))
        assert invalid_count == 2
        assert not is_valid_id(99)  # 9 repeated twice
        assert not is_valid_id(111)  # 1 repeated three times

    def test_range_998_to_1012_has_two_invalid(self):
        """Test example: 998-1012 has two invalid IDs, 999 and 1010."""
        invalid_count = sum(1 for i in range(998, 1013) if not is_valid_id(i))
        assert invalid_count == 2
        assert not is_valid_id(999)  # 9 repeated three times
        assert not is_valid_id(1010)  # 10 repeated twice

    def test_range_1188511880_to_1188511890_has_one_invalid(self):
        """Test example: 1188511880-1188511890 has one invalid ID, 1188511885."""
        invalid_count = sum(
            1 for i in range(1188511880, 1188511891) if not is_valid_id(i)
        )
        assert invalid_count == 1
        assert not is_valid_id(1188511885)

    def test_range_222220_to_222224_has_one_invalid(self):
        """Test example: 222220-222224 has one invalid ID, 222222."""
        invalid_count = sum(1 for i in range(222220, 222225) if not is_valid_id(i))
        assert invalid_count == 1
        assert not is_valid_id(222222)

    def test_range_1698522_to_1698528_has_no_invalid(self):
        """Test example: 1698522-1698528 contains no invalid IDs."""
        invalid_count = sum(1 for i in range(1698522, 1698529) if not is_valid_id(i))
        assert invalid_count == 0

    def test_range_446443_to_446449_has_one_invalid(self):
        """Test example: 446443-446449 has one invalid ID, 446446."""
        invalid_count = sum(1 for i in range(446443, 446450) if not is_valid_id(i))
        assert invalid_count == 1
        assert not is_valid_id(446446)

    def test_range_38593856_to_38593862_has_one_invalid(self):
        """Test example: 38593856-38593862 has one invalid ID, 38593859."""
        invalid_count = sum(1 for i in range(38593856, 38593863) if not is_valid_id(i))
        assert invalid_count == 1
        assert not is_valid_id(38593859)

    def test_patterns_repeated_at_least_twice(self):
        """Test that patterns repeated 2 or more times are invalid."""
        # Patterns repeated exactly twice
        assert is_valid_id(12341234) is False  # 1234 twice
        assert is_valid_id(121121) is False  # 121 twice
        assert is_valid_id(4444) is False  # 44 twice

        # Patterns repeated three times
        assert is_valid_id(123123123) is False  # 123 three times

        # Patterns repeated five times
        assert is_valid_id(1212121212) is False  # 12 five times

        # Patterns repeated seven times
        assert is_valid_id(1111111) is False  # 1 seven times

        # Single digit repeated multiple times
        assert is_valid_id(333) is False  # 3 three times
        assert is_valid_id(5555) is False  # 5 four times

    def test_non_repeating_patterns_are_valid(self):
        """Test that IDs without repeating patterns are valid."""
        assert is_valid_id(12345) is True  # No repeating pattern
        assert is_valid_id(123456) is True  # No repeating pattern
        assert is_valid_id(1234567) is True  # No repeating pattern
        assert is_valid_id(102) is True  # No repeating pattern
        assert is_valid_id(10203) is True  # No repeating pattern
