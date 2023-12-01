#!/usr/bin/env python3

def intersection(s1, s2):
    return (set(s1) & set(s2))

def split(s):
    n = len(s)
    return (s[:n//2], s[n//2:])

def score(c):
    if c >= 'a':
        return ord(c) - 96
    else:
        return ord(c) - 64 + 26

with open("input", encoding="utf-8") as f:
    data = [i for i in f.readlines()]
    total_score = 0
    for s in data:
        item = intersection(*split(s)).pop()
        total_score += score(item)
    print(total_score)
