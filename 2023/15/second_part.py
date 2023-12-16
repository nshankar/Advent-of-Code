import re
from first_part import hash


def parse_step(step):
    pattern = r"^([a-zA-Z]+)(=|-)(\d*)$"
    match = re.match(pattern, step)
    if match:
        label, op, power = match.groups()
    return label, op, int(power) if power else None


def main():
    with open("input.txt", encoding="utf-8") as f:
        steps = map(parse_step, f.read().rstrip().split(","))

    boxes = [dict() for _ in range(256)]
    for label, op, power in steps:
        box = boxes[hash(label)]
        if "=" == op:
            box[label] = power
        else:
            box.pop(label, None)

    s = 0
    for i, box in enumerate(boxes, start=1):
        for j, power in enumerate(box.values(), start=1):
            s += i * j * power
    print(s)


if __name__ == "__main__":
    main()
