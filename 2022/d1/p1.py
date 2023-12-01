from heapq import *

with open("input.txt", encoding="utf-8") as f:
    data = [i for i in f.readlines()]
    max_calories = 0
    curr_elf_calories = 0
    for val in data:
        try:
            curr_elf_calories += int(val)
        except:
            max_calories = max(curr_elf_calories, max_calories)
            curr_elf_calories = 0
    print(max_calories)

with open("input.txt", encoding="utf-8") as f:
    data = [i for i in f.readlines()]
    heap = []
    curr_elf_calories = 0
    for val in data:
        try:
            curr_elf_calories += int(val)
        except:
            heap.append(-curr_elf_calories)
            curr_elf_calories = 0
    heap.append(-curr_elf_calories)
    heapify(heap)
    print(heappop(heap) + heappop(heap) + heappop(heap))
