from numpy import arange

def isValid(seq: str) -> bool:
    """Checks if a String consists ONLY of a repeating sequence"""
    n: int = len(seq)
    if n == 1: return True  # Removes one symbol sequences
    if seq[0] * n == seq: 
        return False
    for i in range(2, n//2+1):
        if n%i==0:
            if seq[:i]*(n//i) == seq:
                return False
    return True


def isValidSiplified(seq: str):
    """Checks if a String consists ONLY of a sequence repeating TWICE"""
    n: int = len(seq)
    if n % 2 == 0 and seq[:n//2] == seq[n//2:]:
        return False
    return True


def part1(in_file: str) -> None:
    """Part 1"""
    sum_invalid_ids = 0
    with open(in_file, 'r') as file:
        ids = ''.join(i.strip() for i in file.readlines()).split(',')
        for id_range in ids:
            id0, id1 = id_range.split('-')
            for num in range(int(id0), int(id1)+1):
                if not isValidSiplified(str(num)):
                    sum_invalid_ids += num
    print('Sum of invalid IDs:', sum_invalid_ids)


def part2(in_file: str) -> None:
    """Part 2"""
    sum_invalid_ids = 0
    with open(in_file, 'r') as file:
        ids = ''.join(i.strip() for i in file.readlines()).split(',')
        for id_range in ids:
            id0, id1 = id_range.split('-')
            for num in range(int(id0), int(id1)+1):
                if not isValid(str(num)):
                    sum_invalid_ids += num
    print('Sum of invalid IDs:', sum_invalid_ids)
        

if __name__ == '__main__':
    part2('AoC2025/Day2/input.txt')