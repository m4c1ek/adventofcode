def task1():
    zero_count = 0
    current_dial_position = 50

    with open("input.txt", "r") as file:
        for line in file:
            data = line.strip()
            direction = 0
            steps = 0
            if data[0] == "L":
                direction = -1
            elif data[0] == "R":
                direction = 1
            steps = int(data[1:])
            current_dial_position = (current_dial_position + direction * steps) % 100
            if current_dial_position == 0:
                zero_count += 1

    print(f"Final dial position: {current_dial_position}")
    print(f"Number of times dial hit zero: {zero_count}")


def move(current_position: int, direction: int, steps: int) -> tuple[int, int]:
    next_position = current_position + direction * steps

    if direction == 1:  # Moving right (clockwise)
        zero_count = next_position // 100
    else:  # Moving left (counter-clockwise)
        zero_count = (current_position - 1) // 100 - (next_position - 1) // 100

    final_position = next_position % 100
    return final_position, zero_count


def parse_line(line: str) -> tuple[int, int]:
    direction = 0
    steps = 0
    if line[0] == "L":
        direction = -1
    elif line[0] == "R":
        direction = 1
    steps = int(line[1:])
    return direction, steps


def task2():
    zero_count = 0
    current_dial_position = 50

    with open("input.txt", "r") as file:
        for line in file:
            data = line.strip()
            direction, steps = parse_line(data)

            current_dial_position, zeros_in_move = move(
                current_dial_position, direction, steps
            )
            zero_count += zeros_in_move

    print(f"Final dial position: {current_dial_position}")
    print(f"Number of times dial hit zero: {zero_count}")


if __name__ == "__main__":
    # task1()
    task2()
