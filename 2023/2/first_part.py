import re
from typing import Tuple


# Constraint
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def extract_cube_counts(text: str):
    red_pattern = r"(\d+)\s*red"
    green_pattern = r"(\d+)\s*green"
    blue_pattern = r"(\d+)\s*blue"

    red_number = re.search(red_pattern, text)
    green_number = re.search(green_pattern, text)
    blue_number = re.search(blue_pattern, text)

    red = int(red_number.group(1)) if red_number else 0
    green = int(green_number.group(1)) if green_number else 0
    blue = int(blue_number.group(1)) if blue_number else 0

    return red, green, blue


def satisfies_constraint(turn: Tuple[int, int, int]):
    return all(x <= y for x, y in zip(turn, (MAX_RED, MAX_GREEN, MAX_BLUE)))


def main():
    with open("input.txt", encoding="utf-8") as file:
        lines = file.readlines()

    games = [line.strip().split(":")[1].split(";") for line in lines]
    s = 0
    for i, game in enumerate(games, start=1):
        turns = map(extract_cube_counts, game)
        if all(map(satisfies_constraint, turns)):
            s += i
    print(s)


if __name__ == "__main__":
    main()
