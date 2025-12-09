def part1(in_file: str) -> None:
    """Part 1"""
    output_joltage = 0
    with open(in_file, 'r') as file:
        banks = [b.strip() for b in file.readlines()]
        for bank in banks:
            n = len(bank)
            max_joltage = int(bank[:2])
            for i in range(0, n-1):
                for j in range(i+1, n):
                    max_joltage = max(int(bank[i]+bank[j]), max_joltage)
            output_joltage += max_joltage
    print('Output joltage:', output_joltage)


def find_max(seq):
    s_max, i_max = int(seq[0]), 0
    for i, s in enumerate(seq):
        if int(s) > s_max:
            s_max, i_max = int(s), i
    return i_max


def part2(in_file: str) -> None:
    """Part 2"""
    output_joltage = 0
    with open(in_file, 'r') as file:
        banks = [b.strip() for b in file.readlines()]
        for bank in banks:
            joltage = ''
            box = bank
            for j in range(12):
                n = len(box) - 11 + j
                i = find_max(box[:n])
                joltage += box[i]
                box = box[i+1:]
                if len(joltage+box) == 12:
                    joltage += box
                    break
            output_joltage += int(joltage)
    print('Output joltage:', output_joltage)


if __name__ == '__main__':
    part2('AoC2025/Day3/input.txt')