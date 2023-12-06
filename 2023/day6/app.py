from functools import reduce

import re
import operator

def get_wins_num(time, record_distance):
    wins_over_record = []
    i = 0
    while i < time:
        if i*(time-i) > record_distance:
            wins_over_record += [i]
            break
        i += 1
    
    j = time
    while j > 0:
        if j*(time-j) > record_distance:
            wins_over_record += [j]
            break
        j -= 1
    return j-i+1

def parse_time_and_distance(input):
    time_pattern = r"Time:\s*([\d\s]+)"
    distance_pattern = r"Distance:\s*([\d\s]+)"

    time_matches = re.search(time_pattern, input)
    distance_matches = re.search(distance_pattern, input)

    if time_matches and distance_matches:
        time_values = list(map(int, time_matches.group(1).split()))
        distance_values = list(map(int, distance_matches.group(1).split()))

        return list(zip(time_values, distance_values))
    return []

def run(file):
    file_content = file.read()
    time_and_distance_pairs = parse_time_and_distance(file_content)
    array = map(lambda pair: get_wins_num(pair[0], pair[1]), time_and_distance_pairs)
    result1 = reduce(operator.mul, array)
    print("assignment 1 = " + str(result1))

    cleaned_text = file_content.replace(" ", "")
    time_and_distance_pairs = parse_time_and_distance(cleaned_text)
    array = map(lambda pair: get_wins_num(pair[0], pair[1]), time_and_distance_pairs)
    result2 = reduce(operator.mul, array)
    print("assignment 2 = " + str(result2))

if __name__ == "__main__":
    with open('input', 'r') as file:
        run(file)