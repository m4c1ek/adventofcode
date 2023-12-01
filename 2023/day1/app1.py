import re

def firstAndLastNumber(text):
    noLetters = re.sub('[a-zA-Z]', '', text)
    return int(noLetters[0] + noLetters[-1])


with open('input', 'r') as file:
    input = file.read().splitlines()
    result = list(map(firstAndLastNumber, input))
    print(sum(result))
    