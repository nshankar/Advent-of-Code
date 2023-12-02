with open("input.txt", encoding="utf-8") as file:
    lines = file.readlines()

s = 0
for line in lines:
    digits = [d for d in line if d.isdigit()]
    s += int(digits[0] + digits[-1])
print(s)
