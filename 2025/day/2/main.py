from typing import Generator


def is_valid_id(id: int) -> bool:
    id_str = str(id)
    length = len(id_str)

    for i in range(1, length // 2 + 1):
        if length % i == 0:
            segment = id_str[:i]
            if segment * (length // i) == id_str:
                return False
    return True


def parse_ranges(filename: str) -> Generator[int, None, None]:
    """Parse ranges from input file and yield all numbers in those ranges."""
    with open(filename, "r") as f:
        content = f.read().strip()

    # Split by commas to get individual ranges
    ranges = content.split(",")

    for range_str in ranges:
        start, end = map(int, range_str.split("-"))
        for num in range(start, end + 1):
            yield num


def count_valid_ids(filename: str) -> tuple[int, int]:
    """Count how many valid IDs exist in the ranges."""
    invalid_sum = 0
    valid_sum = 0
    valid_count = 0
    for id_num in parse_ranges(filename):
        if is_valid_id(id_num):
            valid_count += 1
            valid_sum += id_num
        else:
            invalid_sum += id_num
    return invalid_sum, valid_sum, valid_count


if __name__ == "__main__":
    total_invalid_sum, total_valid_sum, total_valid_count = count_valid_ids("input.txt")
    print(
        f"Total valid IDs: {total_valid_count}, Sum of valid IDs: {total_valid_sum}, Sum of invalid IDs: {total_invalid_sum}"
    )
