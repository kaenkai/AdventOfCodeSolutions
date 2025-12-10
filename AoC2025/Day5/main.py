def part1(in_file: str) -> None:
    """Part 1"""
    with open(in_file, 'r') as file:
        ranges, ingredients = [], []
        for line in file:
            line = line.rstrip()
            if line.isnumeric(): ingredients.append(int(line))
            if '-' in line: ranges.append(line)
        fresh = set()
        fresh_ing = 0
        for i in ingredients:
            for r in ranges:
                mn, mx = r.split('-')
                mn, mx = int(mn), int(mx)
                if mn <= i <= mx:
                    fresh_ing += 1
                    break
        print('Number of fresh ingredients:', fresh_ing)


def part2(in_file: str) -> None:
    """Part 2"""
    with open(in_file, 'r') as file:
        ranges = []
        for line in file:
            line = line.rstrip()
            if '-' in line: 
                mn, mx = line.split('-')
                mn, mx = int(mn), int(mx)
                ranges.append([mn, mx])
        ranges.sort(key=lambda x: x[0])
        ranges_simplified = [ranges[0]]
        for r in ranges[1:]:
            range_included = False
            rs = ranges_simplified[-1]
            if r[0] < rs[1] and r[1] < rs[1]:
                continue
            elif r[0] <= rs[1] and r[1] > rs[1]:
                rs[1] =  r[1]
            elif r[1] > rs[1]:
                ranges_simplified.append(r)
        fresh_ing = 0
        for i, r in enumerate(ranges_simplified):
            fresh_ing += r[1] - r[0] + 1
        print('Number of fresh ingredients:', fresh_ing)


if __name__ == '__main__':
    part2('AoC2025/Day5/input.txt')
