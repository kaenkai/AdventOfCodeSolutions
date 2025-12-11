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
        m = len(worksheet[0])-1  # -1 ommits '\n'
        n = len(worksheet)-1  # -1 ommits operations
        nums = ['']*m
        for i in range(len(worksheet)-1):
            r = worksheet[i][:-1]
            for j, s in enumerate(r):
                nums[j] += s
        nums = [n.strip() for n in nums if n.strip()]
        operations = worksheet[-1].strip().split()
        eq_len = [0]
        for s in worksheet[-1][1:]:
            if not s.strip(): eq_len[-1] += 1
            else: eq_len.append(0)
        eq_len[-1] += 1
        offset = 0
        for i, o in enumerate(operations):
            if o == '+':
                res = 0
                for num in nums[offset:offset+eq_len[i]]: res += int(num)
            elif o == '*':
                res = 1
                for num in nums[offset:offset+eq_len[i]]: res *= int(num)
            grand_total += res
            offset += eq_len[i]
    print('Grand total:', grand_total)


if __name__ == '__main__':
    part2('AoC2025/Day6/input.txt')
