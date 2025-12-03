def part1(sequence_file):
    """Part 1"""
    sequence = 0
    pos = 50
    counter = 0
    print(pos)
    with open(sequence_file, 'r') as file:
        for i in file.readlines():
            rot = int(i[1:])
            if 'R' in  i: pos += rot
            else: pos -= rot
            pos %= 100
            if pos == 0: counter += 1
            print(i.strip(), pos, counter)


def part2(sequence_file):
    """Part 2"""
    sequence = 0
    pos = 50
    counter1, counter2 = 0, 0
    print(pos)
    with open(sequence_file, 'r') as file:
        for i in file.readlines():
            rot = int(i[1:])
            counter2 += rot//100
            rot %= 100
            if 'R' in  i: 
                pos += rot
                if pos > 100: counter2 += 1
            else:
                pos -= rot
                if pos < 0 and pos + rot != 0: counter2 += 1
            pos %= 100
            if pos == 0: counter1 += 1
            info = f'{i.strip()}: {pos} {counter1} {counter2}'
            print(info)
    print(f"Code: {counter1+counter2}")


if __name__ == '__main__':
    part1('AoC2025/Day1/input.txt')  # 6312, 7371
