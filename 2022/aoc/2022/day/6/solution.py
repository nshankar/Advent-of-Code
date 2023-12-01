#!/usr/bin/env python3

from collections import Counter

def find_marker(line):
    # given a string at least 4 long
    letters = Counter(line[:4])
    if len(letters) == 4:
        return 4
    p2 = 4
    while p2 < len(line):
        p1 = p2 - 4
        letters[line[p1]] -= 1
        letters[line[p2]] += 1
        p2 += 1
        if all(letters[k] < 2 for k in letters):
            return p2


with open("input", encoding="utf-8") as f:
    data = f.readlines()

    for line in data:
        print(find_marker(line))
