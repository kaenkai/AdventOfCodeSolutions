"""
@author Karol K
"""

# from string import whitespace
import numpy as np
# from termcolor import colored


input_file = 'Day5/input.txt'


def part1():
    """Part 1"""
    print('Running script for part 1 of day 5 of AoC23')
    with open(input_file, 'r') as file:
        lines = file.readlines()
    seeds = [int(i) for i in lines[0].split(':')[1].strip().split(' ')]
    print('Seeds:', seeds, end='\n\n')
    lines = [i for i in lines[1:] if i != '\n']
    ind = [lines.index(i) for i in lines if ':' in i]
    maps = [lines[i].strip().replace(':', '') for i in ind]
    almanac = {}
    for i in range(len(ind)-1):
        ranges = [j.strip() for j in lines[ind[i]+1:ind[i+1]]]
        almanac[maps[i]] = [[int(n) for n in j.split(' ')] for j in ranges]
    ranges = [j.strip() for j in lines[ind[-1] + 1:]]
    almanac[maps[-1].strip()] = [[int(n) for n in j.split(' ')] for j in ranges]
    for i in almanac:
        print(f'{i}: {almanac[i]}')
    results = {}
    for s in seeds:
        results[s] = []
        v = s
        for m in maps:
            ranges = almanac[m]
            for r in ranges:
                if r[1] <= v <= r[1] + r[2]:
                    v = r[0] + (v - r[1])
                    break
            results[s] += [v]
    for i in results:
        print(f'{i}: {results[i]}')
    locations = [results[i][-1] for i in results]
    print(f'Locations: {locations}')
    lowest_location = min(locations)
    print(f'Lowest location: {lowest_location}')
    return lowest_location


def part2():
    """Part 2"""
    print('Running script for part 2 of day 5 of AoC23')
    with open(input_file, 'r') as file:
        lines = file.readlines()
    seeds_ranges = [int(i) for i in lines[0].split(':')[1].strip().split(' ')]
    seeds_ranges_map = {}
    for i in range(0, len(seeds_ranges)-1, 2):
        seeds_ranges_map[seeds_ranges[i]] = seeds_ranges[i+1]
    for i in seeds_ranges_map:
        print(f'{i}: {seeds_ranges_map[i]}')
        # TODO: optimize, too many seeds
        # print(set(i+np.arange(seeds_ranges_map[i])))
    # print('Length of seeds array:', len(seeds))
    # seeds = set(seeds)
    # print('Length of seeds set:', len(seeds))
    # print('Seeds:', seeds, end='\n\n')
    '''
    lines = [i for i in lines[1:] if i != '\n']
    ind = [lines.index(i) for i in lines if ':' in i]
    maps = [lines[i].strip().replace(':', '') for i in ind]
    almanac = {}
    for i in range(len(ind)-1):
        ranges = [j.strip() for j in lines[ind[i]+1:ind[i+1]]]
        almanac[maps[i]] = [[int(n) for n in j.split(' ')] for j in ranges]
    ranges = [j.strip() for j in lines[ind[-1] + 1:]]
    almanac[maps[-1].strip()] = [[int(n) for n in j.split(' ')] for j in ranges]
    for i in almanac:
        print(f'{i}: {almanac[i]}')
    results = {}
    for s in seeds:
        results[s] = []
        v = s
        for m in maps:
            ranges = almanac[m]
            for r in ranges:
                if r[1] <= v <= r[1] + r[2]:
                    v = r[0] + (v - r[1])
                    break
            results[s] += [v]
    for i in results:
        print(f'{i}: {results[i]}')
    locations = [results[i][-1] for i in results]
    print(f'Locations: {locations}')
    lowest_location = min(locations)
    print(f'Lowest location: {lowest_location}')
    return lowest_location
    '''


if __name__ == '__main__':
    part1()
