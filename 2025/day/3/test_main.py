import pytest
from main import find_largest_number


def test_find_largest_number_case_1():
    """Test case: 987654321111111 -> 98"""
    result = find_largest_number("987654321111111")
    assert result == 98


def test_find_largest_number_case_2():
    """Test case: 811111111111119 -> 89"""
    result = find_largest_number("811111111111119")
    assert result == 89


def test_find_largest_number_case_3():
    """Test case: 234234234234278 -> 78"""
    result = find_largest_number("234234234234278")
    assert result == 78


def test_find_largest_number_case_4():
    """Test case: 818181911112111 -> 92"""
    result = find_largest_number("818181911112111")
    assert result == 92


def test_find_largest_number_12_digit_case_1():
    """Test case: 987654321111111 -> 987654321111 (12 digits)"""
    result = find_largest_number("987654321111111", n=12)
    assert result == 987654321111


def test_find_largest_number_12_digit_case_2():
    """Test case: 811111111111119 -> 811111111119 (12 digits)"""
    result = find_largest_number("811111111111119", n=12)
    assert result == 811111111119


def test_find_largest_number_12_digit_case_3():
    """Test case: 234234234234278 -> 434234234278 (12 digits)"""
    result = find_largest_number("234234234234278", n=12)
    assert result == 434234234278


def test_find_largest_number_12_digit_case_4():
    """Test case: 818181911112111 -> 888911112111 (12 digits)"""
    result = find_largest_number("818181911112111", n=12)
    assert result == 888911112111


if __name__ == "__main__":
    # Run tests manually if not using pytest
    print("Testing 2-digit cases:")
    test_find_largest_number_case_1()
    print("✓ Test case 1 passed: 987654321111111 -> 98")

    test_find_largest_number_case_2()
    print("✓ Test case 2 passed: 811111111111119 -> 89")

    test_find_largest_number_case_3()
    print("✓ Test case 3 passed: 234234234234278 -> 78")

    test_find_largest_number_case_4()
    print("✓ Test case 4 passed: 818181911112111 -> 92")

    print("\nTesting 12-digit cases:")
    test_find_largest_number_12_digit_case_1()
    print("✓ Test case 1 passed: 987654321111111 -> 987654321111")

    test_find_largest_number_12_digit_case_2()
    print("✓ Test case 2 passed: 811111111111119 -> 811111111119")

    test_find_largest_number_12_digit_case_3()
    print("✓ Test case 3 passed: 234234234234278 -> 434234234278")

    test_find_largest_number_12_digit_case_4()
    print("✓ Test case 4 passed: 818181911112111 -> 888911112111")

    print("\nAll tests passed!")
