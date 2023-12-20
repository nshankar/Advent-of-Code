import re


def parse_input(rules, parts):
    pattern = r"(\w+)\{([^}]+)\}"
    parsed_rules = {}
    for rule in rules.split("\n"):
        match = re.match(pattern, rule)
        name, workflow_str = match.groups()  # pyright: ignore
        steps = []
        for step in workflow_str.split(","):
            if ":" in step:
                condition, value = step.split(":")
            else:
                condition, value = "True", step
            steps.append((condition, value))
        parsed_rules[name] = steps

    parsed_parts = []
    for part in parts.split("\n")[:-1]:
        pattern = r"(\w+)=(\d+)"
        matches = re.findall(pattern, part)
        parsed_parts.append({key: int(value) for key, value in matches})  # pyright: ignore
    return parsed_rules, parsed_parts  # pyright: ignore


def main():
    with open("input.txt", encoding="utf-8") as f:
        rules, parts = parse_input(*f.read().split("\n\n"))

    score = 0
    for part in parts:
        x, m, a, s = part["x"], part["m"], part["a"], part["s"]  # noqa
        state = "in"
        while state not in ["A", "R"]:
            for condition, value in rules[state]:
                if eval(condition):
                    state = value
                    break
        if state == "A":
            score += sum(part.values())
    print(score)


if __name__ == "__main__":
    main()
