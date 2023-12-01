#!/usr/bin/env python3
#
def print_data(data):
    for i in range(len(data)):
        print(data[i])
    print()

# given an iterator, returns a T/F array of visibility
def visibility_helper(it):
    visibility = []
    curr = -1
    for i in range(it.__length_hint__()):
        val = next(it)
        if val > curr:
            curr = val
            visibility.append(True)
        else:
            visibility.append(False)
    return visibility


with open("test") as f:
    data = [ [int(c) for c in line[:-1]] for line in f.readlines() ]
    rows = len(data)
    cols = len(data[0])
    print_data(data)

    #West to East
    visible = [visibility_helper(iter(line)) for line in data]
    print_data(visible)


    #East to West
    for i in range(rows):
        it = reversed(data[i])
        helper = visibility_helper(it)
        helper.reverse()
        visible[i] = [any(z) for z in zip(visible[i],  helper)]
    print_data(visible)

    
    #North to South
    for j in range(cols):
        it = iter([data[i][j] for i in range(rows)])
        print([data[i][j] for i in range(rows)])
        helper = visibility_helper(it)
        print('helping:', visible[:][j], helper)
        for i in range(rows):
            visible[i][j] = visible[i][j] or helper[i]
    print_data(visible)

    #South to North
    for j in range(cols):
        it = reversed([data[i][j] for i in range(rows)])
        helper = visibility_helper(it)
        helper.reverse()
        for i in range(rows):
            visible[i][j] = visible[i][j] or helper[i]
    print_data(visible)

    count = 0
    for i in range(rows):
        for j in range(cols):
            if visible[i][j]:
                count += 1
    print(count)
