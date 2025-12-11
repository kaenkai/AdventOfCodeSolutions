def part1(in_file: str) -> None:
    """Part 1"""
    grand_total = 0
    with open(in_file, 'r') as file:
        worksheet = list(zip(*[l.split() for l in file.readlines()]))
        for eq in worksheet:
            nums, op = [int(n) for n in eq[:-1]], eq[-1]
            if op == '+':
                res = 0
                for n in nums: res += n
            elif op == '*':
                res = 1
                for n in nums: res *= n
            grand_total += res
    print('Grand total:', grand_total)


def part2(in_file: str) -> None:
    """Part 2"""
    grand_total = 0
    with open(in_file, 'r') as file:
        worksheet = file.readlines()
        operations = worksheet[-1].strip().split()
        cols = ['']*(len(worksheet[0])-1)
        for i in range(len(worksheet)-1):
            for j, s in enumerate(worksheet[i][:-1]):
                cols[j] += s
        eqns = [[]]
        for eq in [c.strip() for c in cols]:
            if eq: eqns[-1].append(eq)
            else: eqns.append([])
        for i, o in enumerate(operations):
            if o == '+':
                res = 0
                for num in eqns[i]: res += int(num)
            elif o == '*':
                res = 1
                for num in eqns[i]: res *= int(num)
            grand_total += res
    print('Grand total:', grand_total)


if __name__ == '__main__':
    part2('AoC2025/Day6/input.txt')
