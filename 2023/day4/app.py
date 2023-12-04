from functools import reduce
import math

def string_to_int(text):
    return int(text)

def non_empty(text):
    return len(text) > 0

def get_winning_numbers(text):
    dirty_numbers = list(map(lambda x: x.split(' '), text.split(':')[1].split('|')))
    winning_numbers = list(map(string_to_int, filter(non_empty, dirty_numbers[0])))
    my_numbers = list(map(string_to_int, filter(non_empty, dirty_numbers[1])))
    return list(set(my_numbers).intersection(winning_numbers))
    
def get_winning_cards_value(text):
    common_numbers = get_winning_numbers(text)
    count = len(common_numbers)
    return round(math.pow(2, count-1))

def get_cards_cumulation_count(input):
    cards = input.splitlines()
    initial_cards_count = len(cards)
    cards_counts = [1] * initial_cards_count
    
    for i in range(initial_cards_count):
        winning_cards_number = len(get_winning_numbers(cards[i]))
        if winning_cards_number > 0:
            current_card_count = cards_counts[i]
            for j in range(winning_cards_number):
                cards_counts[i+j+1] += current_card_count
    
    return sum(cards_counts)

def run(file):
    file_content = file.read()
    input = file_content.splitlines()
    cards = list(map(get_winning_cards_value, input))
    print("assignment 1 = " + str(sum(cards)))

    cards_cumulation_count = get_cards_cumulation_count(file_content)
    print("assignment 2 = " + str(cards_cumulation_count))

if __name__ == "__main__":
    with open('input', 'r') as file:
        run(file)
    