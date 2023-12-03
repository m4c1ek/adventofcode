import re
from functools import reduce

non_keyboard_chars = [chr(code) for code in range(0x2500, 0x26FF)]
def get_part_numbers_in_row(three_rows):
    three_rows_mapped = list(map(lambda x: "." + x + ".", three_rows))
    number_matches = re.finditer(r'\d+', three_rows_mapped[1])
    number_indexes = [(match.start(), match.end(), match.group()) for match in number_matches]
    part_numbers = []
    for index in number_indexes:
        index_start = index[0]-1
        index_end = index[1]+1
        text_to_check_for_symbols = three_rows_mapped[0][index_start:index_end] + three_rows_mapped[1][index_start:index_end] + three_rows_mapped[2][index_start:index_end]
        symbols = text_to_check_for_symbols.replace(index[2], "").replace(".", "")
        if (len(symbols) > 0):
            part_numbers.append(index[2])
    return part_numbers

def get_part_numbers(input):
    dots_string = "." * len(input[0])
    with_extra_lines = [dots_string] + input + [dots_string]
    result = []
    for i in range(len(with_extra_lines)-2):
        result += get_part_numbers_in_row(with_extra_lines[i:i+3])
    return result

def get_half_gears_in_row(three_rows):
    three_rows_mapped = list(map(lambda x: "." + x + ".", three_rows))
    number_matches = re.finditer(r'\d+', three_rows_mapped[1])
    number_indexes = [(match.start(), match.end(), match.group()) for match in number_matches]
    gears = {}
    for index in number_indexes:
        index_start = index[0]-1
        index_end = index[1]+1
        text_to_check_for_symbols = three_rows_mapped[0][index_start:index_end] + three_rows_mapped[1][index_start:index_end] + three_rows_mapped[2][index_start:index_end]
        filtered_string = ''.join(char for char in text_to_check_for_symbols if char in non_keyboard_chars)
        char_list = [char for char in filtered_string]
        
        for char in char_list:
            if char in gears:
                gears[char] += [index[2]]
            else:
                gears[char] = [index[2]]
    return gears 

def get_gears(file_content):
    i = 0
    while '*' in file_content:
        file_content = file_content.replace('*', non_keyboard_chars[i], 1)
        i += 1
    input = file_content.splitlines()
    dots_string = "." * len(input[0])
    with_extra_lines = [dots_string] + input + [dots_string]
    result = {}
    for i in range(len(with_extra_lines)-2):
        half_gears = get_half_gears_in_row(with_extra_lines[i:i+3])
        for key in half_gears:
            if key in result:
                result[key] += half_gears[key]
            else:
                result[key] = half_gears[key]
    return result


def run(file):
    file_content = file.read()
    input = file_content.splitlines()
    part_numbers = get_part_numbers(input)
    sum_of_part_numbers = sum(map(int, part_numbers))
    print("assignment 1 = " + str(sum_of_part_numbers))

    input = file.read()
    gears = get_gears(file_content)
    list_of_gears = list(filter(lambda x: len(x) == 2, gears.values()))
    gears_multiplied = list(map(lambda x: int(x[0]) * int(x[1]), list_of_gears))
    print("assignment 2 = " + str(sum(gears_multiplied)))


if __name__ == "__main__":
    with open('input', 'r') as file:
        run(file)
    