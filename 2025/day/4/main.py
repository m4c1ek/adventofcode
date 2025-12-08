import numpy as np


def __count_adjacent_at_symbols(array: np.ndarray) -> np.ndarray:
    height, width = array.shape
    counts = np.zeros((height, width), dtype=int)
    for y in range(0, height):
        for x in range(0, width):
            if array[y, x] != "@":
                counts[y, x] = -1
                continue

            count = sum(
                1
                for dy in [-1, 0, 1]
                for dx in [-1, 0, 1]
                if (dy != 0 or dx != 0)
                and 0 <= y + dy < height
                and 0 <= x + dx < width
                and array[y + dy, x + dx] == "@"
            )
            counts[y, x] = count
    return counts


def count_where_adjacent_at_symbols_less_equal(s: str, n: int) -> int:
    array = np.array([list(line.strip()) for line in s.splitlines()])
    counts = __count_adjacent_at_symbols(array)
    return np.sum((counts <= n) & (counts >= 0))


def count_and_replace_with_dot_where_adjacent_at_symbols_less_equal(
    array: np.ndarray, n: int
) -> int:
    counts = __count_adjacent_at_symbols(array)
    count = np.sum((counts <= n) & (counts >= 0))
    if count > 0:
        array[(counts <= n) & (counts >= 0)] = "."
        count += count_and_replace_with_dot_where_adjacent_at_symbols_less_equal(
            array, n
        )
    return count


if __name__ == "__main__":
    result_sum = 0
    with open("input.txt", "r") as file:
        input_data = file.read()
        array = np.array([list(line.strip()) for line in input_data.splitlines()])
        result_sum = count_and_replace_with_dot_where_adjacent_at_symbols_less_equal(
            array, n=3
        )
    print(f"Result: {result_sum}")
