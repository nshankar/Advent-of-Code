from typing import Iterable
from itertools import chain


def iter_rfind(s: str, substrs: Iterable[str]):
    "Search s for an iterable of potential substrings. Return the index of the last match and the last match."
    positions = [(s.rfind(substr), substr) for substr in substrs]
    # rfind returns -1 if the substr is not present
    filtered_positions = filter(lambda x: x[0] >= 0, positions)
    return max(filtered_positions)


def iter_find(s: str, substrs: Iterable[str]):
    "Search s for an iterable of potential substrings. Return the index of the first match and the first match."
    positions = [(s.find(substr), substr) for substr in substrs]
    # find returns -1 if the substr is not present
    filtered_positions = filter(lambda x: x[0] >= 0, positions)
    return min(filtered_positions)


decoder = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_calibration_value(line: str):
    first_digit = iter_find(line, chain(decoder.keys(), decoder.values()))[1]
    last_digit = iter_rfind(line, chain(decoder.keys(), decoder.values()))[1]

    return int(
        "".join(
            map(lambda d: d if d.isdigit() else decoder[d], (first_digit, last_digit))
        )
    )


with open("input.txt", encoding="utf-8") as file:
    lines = file.readlines()
s = sum(map(get_calibration_value, lines))
print(s)
