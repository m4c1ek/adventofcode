def __merge_and_sort_ranges(ranges):
    ranges = sorted(ranges)
    merged = []
    for s, e in ranges:
        if not merged or s > merged[-1][1]:
            merged.append([s, e])
        else:
            merged[-1][1] = max(merged[-1][1], e)
    return merged


def __number_in_ranges(number: int, ranges):
    for s, e in ranges:
        if s <= number <= e:
            return True
    return False


def __total_numbers_in_ranges(ranges):
    count = 0
    for s, e in ranges:
        count += e - s + 1
    return count


if __name__ == "__main__":
    ranges = []
    numbers = []
    counts = 0

    with open("input.txt", "r") as file:
        for line in file:
            if not line.strip():
                continue

            if "-" in line:
                start, end = map(int, line.strip().split("-"))
                ranges.append([start, end])
            else:
                numbers.append(int(line.strip()))

    merged_sorted_ranges = __merge_and_sort_ranges(ranges)
    sorted_numbers = sorted(numbers)

    for number in sorted_numbers:
        if __number_in_ranges(number, merged_sorted_ranges):
            counts += 1

    total_numbers = __total_numbers_in_ranges(merged_sorted_ranges)
    print(f"Total numbers in ranges: {total_numbers}")
    print(f"Count of numbers within ranges: {counts}")
