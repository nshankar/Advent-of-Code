#!/usr/bin/env python3
import numpy as np

direction_dict = {
    'R': np.array([1,0]),
    'U': np.array([0,1]),
    'L': np.array([-1, 0]),
    'D': np.array([0,-1])
}
def norm2(x):
    return x[0]**2 + x[1]**2

def helper(x):
    return np.array([x[0]//abs(x[0]),
                     x[1]//abs(x[1])])

def move_tail(H,T):
    d = norm2(H - T)
    if d == 4:
        #step tail 1 step towards head
        T += (H-T)//2
        pass
    elif d == 5:
        #step tail diagonally towards head
        T += helper(H-T)
    return T

def move_pair(H, T, move):
    #first move H
    direction, steps = move
    step = direction_dict[direction]
    for i in range(steps):
        H += step
        T = move_tail(H, T)
        positions.add(tuple(T))
        # print(H, T)

with open("input") as f:
    data = []
    for line in f.readlines():
        direction, steps = line.split()
        data.append([direction, int(steps)])

positions = set()
H = np.array([0,0])
T = np.array([0,0])
for move in data:
    move_pair(H, T, move)
print(len(positions))
