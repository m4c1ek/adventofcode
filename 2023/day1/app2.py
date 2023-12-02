import re

def replaceTextsToNumbers(text):
    return text.replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4").replace("five", "5").replace("six", "6").replace("seven", "7").replace("eight", "8").replace("nine", "9")

def normalizeText(text):
    return text.replace("one", "oonee").replace("two", "ttwoo").replace("three", "tthreee").replace("four", "ffourr").replace("five", "ffivee").replace("six", "ssixx").replace("seven", "ssevenn").replace("eight", "eeightt").replace("nine", "nninee")

def get_first_and_last(raw_text):
    text = normalizeText(raw_text)
    words = re.findall("(?i)one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9|0", text)
    first_and_last = []
    if len(words) > 0:
        match = re.search(r'one|two|three|four|five|six|seven|eight|nine|\d', text)
        match_reverse = re.search(r'eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d', text[::-1])
        first_and_last = [match.group(), match_reverse.group()[::-1]]

    first_and_last_numbers = map(replaceTextsToNumbers, first_and_last)
    final = int("".join(first_and_last_numbers))
    return final

def run(file):
    input = file.read().splitlines()
    result = list(map(get_first_and_last, input))
    print("assignment 2 = " + str(sum(result)))
        
if __name__ == "__main__":
    with open('input', 'r') as file:
        run(file)