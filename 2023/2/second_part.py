from first_part import extract_cube_counts
from math import prod

with open("input.txt", encoding="utf-8") as file:
    lines = file.readlines()

games = [line.strip().split(":")[1].split(";") for line in lines]
s = 0
for game in games:
    turns = map(extract_cube_counts, game)
    turns_transposed = [list(c) for c in zip(*turns)]
    s += prod(map(max, turns_transposed))
print(s)
