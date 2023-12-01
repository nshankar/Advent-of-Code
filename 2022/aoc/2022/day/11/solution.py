#!/usr/bin/env python3
from queue import Queue

def parse_input(data):
    monkeys = []
    n = 1
    while n < len(data):
        starting_items = get_starting_items(data[n])
        n+=1
        operation = get_operation(data[n])
        n+=1
        test = get_test(data[n:n+3])
        n+=5
        monkeys.append(Monkey(starting_items, operation, test))
    return monkeys

def get_starting_items(line):
    numstrings = line.split(':')[1].split(',')
    return [int(i) for i in numstrings]

def get_operation(line):
    op, num = line.split()[-2:]
    #special case
    if num == "old":
        if op == '*':
            return lambda x: x**2
        elif op == '+':
            return lambda x: 2*x

    if op == '+':
        return lambda x: x + int(num)
    elif op == '*':
            return lambda x: x * int(num)
    # something went wrong
    return None

def get_test(lines):
    divisor = int(lines[0].split()[-1])
    true_case = int(lines[1].split()[-1])
    false_case = int(lines[2].split()[-1])
    return divisor, true_case, false_case

class Monkey:
    def __init__(self, starting_items, operation, test):
        self.items = Queue(maxsize=-1)
        for item in starting_items:
            self.items.put(item)
        self.operation = operation
        self.divisor = test[0]
        self.true_case = test[1]
        self.false_case = test[2]
        self.counter = 0

    def test(self, worry):
        if worry % self.divisor == 0:
            return self.true_case
        return self.false_case

    def empty(self):
        return self.items.qsize() == 0

    def inspect_and_throw(self):
        item = self.items.get()
        item = self.operation(item)//3
        monkey = self.test(item)
        self.counter += 1
        return item, monkey

    def catch(self, item):
        self.items.put(item)

    def get_counter(self):
        return self.counter

    def print(self):
        print(self.items)
        print(self.operation)
        print("divisor: ", self.divisor)
        print("true_case: ", self.true_case)
        print("false_case: ", self.false_case)

with open("input") as f:
    monkeys = parse_input(f.readlines())

for round in range(20):
    for monkey in monkeys:
        while not monkey.empty():
            item, idx = monkey.inspect_and_throw()
            monkeys[idx].catch(item)

print([monkey.get_counter() for monkey in monkeys])
