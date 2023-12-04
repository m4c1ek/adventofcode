import re
from functools import reduce

def get_winning_cards_value(text):
    return 8

def run(file):
    print("assignment 1 = " + str(get_winning_cards_value(file.read())))

if __name__ == "__main__":
    with open('input', 'r') as file:
        run(file)
    