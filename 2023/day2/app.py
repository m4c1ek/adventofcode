import re
from functools import reduce

def get_colors(text):
    matches = re.findall(r'(\d+)\s*([a-zA-Z]+)', text)
    colors = {color: int(number) for number, color in matches}
    return {
        "red": colors.get('red', 0),
        "green": colors.get('green', 0),
        "blue": colors.get('blue', 0)
    }

def max_colors(colors1, colors2):
    return {
        "red": max(colors1["red"], colors2["red"]),
        "green": max(colors1["green"], colors2["green"]),
        "blue": max(colors1["blue"], colors2["blue"])
    }

def get_valid_colors(text):
    colors = get_colors(text)
    reds_valid = colors["red"] < 13
    greens_valid = colors["green"] < 14
    blues_valid = colors["blue"] < 15
    return reds_valid and greens_valid and blues_valid

def get_min_cubes(text):
    game_and_choices = text.split(':')
    choices = game_and_choices[1].split(';')
    choices = list(map(lambda x: get_colors(x), choices))
    reduced_choices = reduce(max_colors, choices, {"red": 0, "green": 0, "blue": 0})
    return [reduced_choices["red"], reduced_choices["green"], reduced_choices["blue"]]

def get_possible_game(text):
    game_and_choices = text.split(':')
    game_number = int(game_and_choices[0].split(' ')[1])
    choices = game_and_choices[1].split(';')
    choices = list(map(lambda x: get_valid_colors(x), choices))
    choices_valid = all(choices)
    if choices_valid:
        return game_number
    else:
        return None

def run(file):
    input = file.read().splitlines()
    result_possible = list(map(get_possible_game, input))
    result_no_nones = list(filter(lambda x: x is not None, result_possible))
    print("assignment 1 = " + str(sum(result_no_nones)))

    result_min_cubes = list(map(get_min_cubes, input))
    result_power = list(map(lambda x: x[0] * x[1] * x[2], result_min_cubes))
    print("assignment 2 = " + str(sum(result_power)))

if __name__ == "__main__":
    with open('input', 'r') as file:
        run(file)
    