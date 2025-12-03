def find_largest_number(number_as_text: str, n: int = 2) -> int:
    """
    Find the largest n-digit number by selecting n digits from the input string
    in the order they appear, maximizing the resulting number.

    Args:
        number_as_text: The input string containing digits
        n: Number of digits to select (default: 2)

    Returns:
        The largest n-digit number possible
    """
    length = len(number_as_text)

    if length < n:
        raise ValueError(f"Input must have at least {n} digits")

    result = []
    start_index = 0

    # For each position in the result, find the largest digit
    # that still leaves enough digits for the remaining positions
    for position in range(n):
        remaining_positions = n - position - 1
        # We need to leave at least 'remaining_positions' digits after our choice
        search_end = length - remaining_positions

        # Find the largest digit in the valid range
        max_digit = -1
        max_index = -1

        for i in range(start_index, search_end):
            digit = int(number_as_text[i])
            if digit > max_digit:
                max_digit = digit
                max_index = i

        result.append(str(max_digit))
        start_index = max_index + 1

    return int("".join(result))


if __name__ == "__main__":
    result_sum = 0
    with open("input.txt", "r") as file:
        for line in file:
            content = line.strip()
            result = find_largest_number(content, n=12)
            result_sum += result

    print("Result:", result_sum)
