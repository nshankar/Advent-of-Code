#!/usr/bin/env python3
def complete_cycle(cycle, register, strength):
    cycle += 1
    if cycle % 40 == 0:
        strength += (cycle+20) * register
    return cycle, strength

instruction_set = {'addx': 2, 'noop': 1}
with open("test") as f:
    data = [line.split() for line in f.readlines()]

cycle = -20
register = 1
strength = 0
for instruction in data:
    cycle, strength = complete_cycle(cycle, register, strength)
    if instruction_set[instruction[0]] == 2:
        cycle, strength = complete_cycle(cycle, register, strength)
        register += int(instruction[1])
print(strength)
