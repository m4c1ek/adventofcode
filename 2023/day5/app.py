import re

class Mapping:
    def __init__(self, destination_range_start, source_range_start, range_length):
        self.destination_range_start = destination_range_start
        self.source_range_start = source_range_start
        self.range_length = range_length

    def __str__(self) -> str:
        return f"destination_range_start: {self.destination_range_start}, source_range_start: {self.source_range_start}, range_length: {self.range_length}"

class Mappings:
    def __init__(self, source_category, destination_category, mappings: [Mapping]) -> None:
        self.source_category = source_category
        self.destination_category = destination_category
        self.mappings = mappings
    
    def __str__(self) -> str:
        mappings_str = "\n\t".join(str(mapping) for mapping in self.mappings)
        return f"source_category:\n\t{self.source_category}\ndestination_category:\n\t{self.destination_category}\nmappings:\n\t{mappings_str}"

def get_mapping(input):
    lines = input.strip().split("\n")
    source_category, destination_category = lines[0].split(" ")[0].strip().split("-to-")
    mappings = [Mapping(*map(int, line.split())) for line in lines[1:]]
    mappings_obj = Mappings(source_category, destination_category, mappings)
    return mappings_obj

def get_mappings(input):
    return list(map(get_mapping, filter(lambda x: "map:" in x, input.split("\n\n"))))

def get_location(seed, all_mappings):
    current_seed = seed
    source_category = "seed"
    while source_category != "location":
        mappings = next(mapping for mapping in all_mappings if mapping.source_category == source_category)
        source_category = mappings.destination_category
        try:
            mapping = next(mapping for mapping in mappings.mappings if mapping.source_range_start <= current_seed <= mapping.source_range_start + mapping.range_length)
        except StopIteration:
            0
        else:
            current_seed = current_seed - mapping.source_range_start + mapping.destination_range_start
    return current_seed

def get_seeds(input):
    seeds = re.findall(r'seeds:\s([\d\s]+)', input)
    seeds = [int(seed) for seed in seeds[0].split()]
    return seeds

def get_location_from_range(start_seed, range_length, all_mappings, iteration):
    num_ranges = 1000
    if num_ranges > range_length:
        num_ranges = range_length
    step_size = range_length // (num_ranges - 1)
    more_seeds = [start_seed + i * step_size for i in range(num_ranges)]+[start_seed + range_length]
    if step_size == 1:
        more_seeds = [start_seed + i * step_size for i in range(range_length)]+[start_seed + range_length]
    locations = list(map(lambda seed: get_location(seed, all_mappings), more_seeds))
    if step_size == 1:
        return min(locations)
    
    min_location = locations.index(min(locations))
    min_location_seed = more_seeds[min_location]
    new_start_seed = max(min_location_seed - range_length // 4, start_seed)
    new_range_length = range_length // 2
    return get_location_from_range(new_start_seed, new_range_length, all_mappings, iteration + 1)
    
def run(file):
    file_content = file.read()
    seeds = get_seeds(file_content)
    all_mappings = get_mappings(file_content)
    locations = list(map(lambda seed: get_location(seed, all_mappings), seeds))
    print("assignment 1 = " + str(min(locations)))
    
    seeds_pairs = []
    for i in range(0, len(seeds), 2):
        pair = seeds[i:i+2]
        seeds_pairs.append(pair)
    min_locations = list(map(lambda pair: get_location_from_range(pair[0], pair[1], all_mappings, 0), seeds_pairs))
    print("assignment 2 = " + str(min(min_locations)))

if __name__ == "__main__":
    with open('input', 'r') as file:
        run(file)
    