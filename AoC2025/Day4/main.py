def part1(in_file: str) -> None:
    """Part 1"""
    accessable_paper_rolls = 0
    with open(in_file, 'r') as file:
        diagram = [list('.' + b.strip() + '.') for b in file.readlines()]
        m = len(diagram[0])
        diagram = [['.']*m] + diagram + [['.']*m]
        n = len(diagram)
        # n: # of rows; m: # of columns
        for i in range(1, n-1):
            for j in range(1, m-1):
                if diagram[i][j] == '@':
                    neighbors = diagram[i-1][j-1:j+2] + diagram[i][j-1:j+2] + diagram[i+1][j-1:j+2]
                    if neighbors.count('@') + neighbors.count('X') < 5:
                        accessable_paper_rolls += 1
                        diagram[i][j] = 'X'
    print('Rolls of paper that can be accessed by a forklift:', accessable_paper_rolls)


def remove_rolls(diagram) -> int:
    """Removes paper rolls"""
    m, n = len(diagram[0]), len(diagram)
    paper_rolls_removed = 0
    for i in range(1, n-1):
        for j in range(1, m-1):
            if diagram[i][j] == '@':
                neighbors = diagram[i-1][j-1:j+2] + diagram[i][j-1:j+2] + diagram[i+1][j-1:j+2]
                if neighbors.count('@') + neighbors.count('X') < 5:
                    paper_rolls_removed += 1
                    diagram[i][j] = 'X'
    for i in range(1, n-1):
        for j in range(1, m-1):
            if diagram[i][j] == 'X': diagram[i][j] = '.'
    return paper_rolls_removed


def part2(in_file: str) -> None:
    """Part 2"""
    rolls_removed = 0
    with open(in_file, 'r') as file:
        diagram = [list('.' + b.strip() + '.') for b in file.readlines()]
        m = len(diagram[0])
        diagram = [['.']*m] + diagram + [['.']*m]
        n = len(diagram)
        # n: # of rows; m: # of columns
        x = remove_rolls(diagram)
        while x > 0:
            rolls_removed += x
            x = remove_rolls(diagram)
    print('Rolls of paper removed by a forklift:', rolls_removed)


if __name__ == '__main__':
    part2('AoC2025/Day4/input.txt')