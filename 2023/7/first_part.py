from collections import Counter
from functools import total_ordering
from enum import Enum


@total_ordering
class Hand:
    card_to_int = {str(k): k for k in range(2, 10)}
    card_to_int.update({"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14})

    @total_ordering
    class HandType(Enum):
        HIGH_CARD = 1
        PAIR = 2
        TWO_PAIR = 3
        THREE_OF_A_KIND = 4
        FULL_HOUSE = 5
        FOUR_OF_A_KIND = 6
        FIVE_OF_A_KIND = 7

        def __eq__(self, other):
            return self.value == other.value

        def __lt__(self, other):
            return self.value < other.value

    def __init__(self, cards):
        self.cards = cards
        self.hand_type = self.parse_hand_type(cards)

    def parse_cards(self, cards):
        return tuple(self.card_to_int[c] for c in cards)

    def parse_hand_type(self, cards):
        counter = Counter(cards)
        values = tuple(sorted(counter.values()))
        if values == (5,):
            return self.HandType.FIVE_OF_A_KIND
        elif values == (1, 4):
            return self.HandType.FOUR_OF_A_KIND
        elif values == (2, 3):
            return self.HandType.FULL_HOUSE
        elif values == (1, 1, 3):
            return self.HandType.THREE_OF_A_KIND
        elif values == (1, 2, 2):
            return self.HandType.TWO_PAIR
        elif values == (1, 1, 1, 2):
            return self.HandType.PAIR
        else:
            return self.HandType.HIGH_CARD

    def __eq__(self, other):
        return self.hand_type == other.hand_type and self.parse_cards(
            self.cards
        ) == self.parse_cards(other.parse_cards)

    def __lt__(self, other):
        if self.hand_type == other.hand_type:
            return self.parse_cards(self.cards) < self.parse_cards(other.cards)
        return self.hand_type < other.hand_type

    def __repr__(self):
        return self.cards


def main():
    with open("input.txt", encoding="utf-8") as file:
        raw_data = [line.strip() for line in file.readlines()]
    data = [(Hand(line.split()[0]), int(line.split()[1])) for line in raw_data]
    data.sort(key=lambda x: x[0])
    winnings = sum([i * data[i - 1][1] for i in range(1, len(data) + 1)])
    print(winnings)


if __name__ == "__main__":
    main()
