def main():
    with open("input.txt", encoding="utf-8") as file:
        cards = [line.strip() for line in file.readlines()]

    cards = [
        map(lambda y: map(int, y.split()), x.split(":")[1].split("|")) for x in cards
    ]

    s = 0
    for numbers, winning_numbers in cards:
        intersection = set(numbers) & set(winning_numbers)
        if len(intersection) > 0:
            s += pow(2, len(intersection) - 1)
    print(s)


if __name__ == "__main__":
    main()
