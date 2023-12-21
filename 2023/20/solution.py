from queue import SimpleQueue
from math import lcm


def parse_input(lines):
    broadcaster = []
    flipflop = {}
    conjunction = {}

    for line in lines:
        module, neighbors_str = line.split(" -> ")
        neighbors = neighbors_str.rstrip().split(", ")
        if module[0] == "%":
            flipflop[module[1:]] = [OFF, neighbors]
        elif module[0] == "&":
            conjunction[module[1:]] = [{}, neighbors]
        else:
            broadcaster.extend(neighbors)

    # prefill conjunction with predecessors
    for line in lines:
        module, neighbors_str = line.split(" -> ")
        neighbors = neighbors_str.rstrip().split(", ")
        for nbr in neighbors:
            if nbr in conjunction:
                conjunction[nbr][0][module[1:]] = LOW

    return broadcaster, flipflop, conjunction


def get_period_dict():
    # determine through examination of input data
    special_conjunctions = ("qz", "sk", "sv", "dr")
    period_dict = {}
    for sc in special_conjunctions:
        for pred in conjunction[sc][0]:
            period_dict[(pred, sc, HIGH)] = []
    return period_dict


def send_pulse(sender, receiver, pulse_type):
    counter[pulse_type] += 1
    new_pulses = []
    if receiver in flipflop and pulse_type == LOW:
        flipflop[receiver][0] = not flipflop[receiver][0]  # flip
        for nbr in flipflop[receiver][1]:
            # cheat on pulse_type by overloading
            new_pulses.append((receiver, nbr, flipflop[receiver][0]))
    elif receiver in conjunction:
        conjunction[receiver][0][sender] = pulse_type
        new_pulse_type = not all(conjunction[receiver][0].values())
        for nbr in conjunction[receiver][1]:
            new_pulses.append((receiver, nbr, new_pulse_type))
    return new_pulses


def main():
    pulseq = SimpleQueue()
    period_dict = get_period_dict()
    for i in range(100000):
        counter[LOW] += 1  # button to broadcaster
        for module in broadcaster:
            pulseq.put(("broadcaster", module, LOW))
        while pulseq.qsize():
            new_pulses = send_pulse(*pulseq.get())
            for pulse in new_pulses:
                if pulse in period_dict:
                    period_dict[pulse].append(i)
                pulseq.put(pulse)
        # Part 1
        if i == 1000:
            print("Part 1:", counter[LOW] * counter[HIGH])

    # Part 2
    ans = []
    for _, v in period_dict.items():
        diffs = [v[-i] - v[-i - 1] for i in range(1, len(v) - 1)]
        # determine through examination of input data
        if len(set(diffs)) == 1:
            ans.append(diffs[-1])
    print("Part 2:", lcm(*ans))


if __name__ == "__main__":
    HIGH, LOW = True, False
    ON, OFF = True, False
    with open("input.txt", encoding="utf-8") as f:
        broadcaster, flipflop, conjunction = parse_input(f.readlines())
    counter = {LOW: 0, HIGH: 0}
    main()
