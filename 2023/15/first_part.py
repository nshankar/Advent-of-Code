def hash(word):
    s = 0
    for c in word:
        s += ord(c)
        s *= 17
    return s % 256


def main():
    with open("input.txt", encoding="utf-8") as f:
        steps = f.read().rstrip().split(",")
    print(sum(map(hash, steps)))


if __name__ == "__main__":
    main()
