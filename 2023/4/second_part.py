def main():
    with open("input.txt", encoding="utf-8") as file:
        cards = [line.strip() for line in file.readlines()]

    cards = [
        map(lambda y: map(int, y.split()), x.split(":")[1].split("|")) for x in cards
    ]

    memo = [1] * len(cards)
    for i, card in enumerate(cards):
        numbers, winning_numbers = card
        intersection = set(numbers) & set(winning_numbers)
        if len(intersection) > 0:
            for j in range(i + 1, i + len(intersection) + 1):
                memo[j] += memo[i]
    print(sum(memo))


if __name__ == "__main__":
    main()
