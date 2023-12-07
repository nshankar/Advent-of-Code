from collections import Counter
from first_part import Hand


class JokerHand(Hand):
    card_to_int = card_to_int = {str(k): k for k in range(2, 10)}
    # Jack is now the weakest card
    card_to_int.update({"T": 10, "J": 1, "Q": 12, "K": 13, "A": 14})

    def __init__(self, cards):
        super().__init__(cards)

    def parse_hand_type(self, cards):
        # Jack behaves like a Joker
        counter = Counter(cards)
        if counter["J"] and len(counter) > 1:
            counter.pop("J")
            argmax = max(counter, key=counter.get)
            cards = cards.replace("J", argmax)
        return super().parse_hand_type(cards)


def main():
    with open("input.txt", encoding="utf-8") as file:
        raw_data = [line.strip() for line in file.readlines()]
    data = [(JokerHand(line.split()[0]), int(line.split()[1])) for line in raw_data]
    data.sort(key=lambda x: x[0])
    winnings = sum([i * data[i - 1][1] for i in range(1, len(data) + 1)])
    print(winnings)


if __name__ == "__main__":
    main()
