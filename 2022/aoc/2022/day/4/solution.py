#!/usr/bin/env python3
import re
def parse_line(l):
    ranges = list(map(int, re.split(r'\D+',l)[:-1]))
    return ranges[:2], ranges[2:]

# returns true if r contains s else false
def contains(r, s):
    return s[0] >= r[0] and s[1] <= r[1]

with open("input", encoding="utf-8") as f:
    data = [i for i in f.readlines()]
    count = 0
    for line in data:
        r,s = parse_line(line)
        if contains(r,s) or contains(s,r):
            count += 1
    print(count)
