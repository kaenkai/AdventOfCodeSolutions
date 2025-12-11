def part1(in_file: str) -> None:
    """Part 1"""
    with open(in_file, 'r') as file:
        worksheet = list(zip(*[l.split() for l in file.readlines()]))
        grand_total = 0
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
                
if __name__ == '__main__':
    part1('AoC2025/Day6/input.txt')