from functools import reduce
import math

def string_to_int(text):
    return int(text)

def non_empty(text):
    return len(text) > 0

def get_winning_cards_value(text):
    dirty_numbers = list(map(lambda x: x.split(' '), text.split(':')[1].split('|')))
    winning_numbers = list(map(string_to_int, filter(non_empty, dirty_numbers[0])))
    my_numbers = list(map(string_to_int, filter(non_empty, dirty_numbers[1])))
    common_numbers = list(set(my_numbers).intersection(winning_numbers))
    count = len(common_numbers)
    return round(math.pow(2, count-1))

def run(file):
    input = file.read().splitlines()
    cards = list(map(get_winning_cards_value, input))
    print("assignment 1 = " + str(sum(cards)))

if __name__ == "__main__":
    with open('input', 'r') as file:
        run(file)
    