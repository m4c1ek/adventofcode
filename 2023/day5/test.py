import pytest
from app import get_location, get_seeds, get_mappings

all_input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

@pytest.mark.skip(reason="not ready")
@pytest.mark.parametrize(
    "input, seeds",
    [
        (all_input, [79, 14, 55, 13])
    ],
)
def test_get_seeds(input, seeds):
    assert get_seeds(input) == seeds 

mapping_input = """seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

# @pytest.mark.skip(reason="not ready")
@pytest.mark.parametrize(
    "seed, location",
    [
        (79, 82),
        (14, 43),
        (55, 86),
        (13, 35)
    ],
)
def test_get_location(seed, location):
    assert get_location(seed, all_input) == location

@pytest.mark.skip(reason="not ready")
def test_get_mappings():
    mappings = get_mappings(all_input)
    for mapping in mappings:
        print("\n")
        print(mapping)
    
    assert(len(mappings) == 7)
# Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
# Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
# Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
# Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.