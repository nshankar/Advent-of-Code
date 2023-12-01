#!/usr/bin/env python3

# Optimal data structure is probs an array of linked lists
# This is python though lol

#prints sideways
def print_state(state):
    for stack in state:
        print(stack)

def initialize_state(initial_data):
    num_stacks = len(initial_data[-1].split())
    # parse initial lines to build a data structure
    stacks = [ [] for j in range(num_stacks) ]
    for i in range(n-1, -1, -1):
        line = initial_data[i]
        for pos in range(1,len(line),4):
            crate = line[pos]
            if crate != ' ':
                j = (pos-1)//4
                stacks[j].append(crate)
    return stacks

# a move is a tuple (x,y,z) move x from y to z
def process_move(move, state):
    x,y,z = move
    # indexing issue
    y -= 1
    z -= 1
    for i in range(x):
        state[z].append(state[y].pop())

with open("input", encoding="utf-8") as f:
    data = f.readlines()
    # find out which part is initial data
    n = 0
    while data[n][1] != '1':
        n+=1
    stacks = initialize_state(data[:n])

    print_state(stacks)
    for line in data[n+2:]:
        move = [int(line.split()[2*i+1]) for i in range(3)]
        print(move)
        process_move(move, stacks)


    for stack in stacks:
        print(stack[-1], end='')
    print()
