#!/usr/bin/env python3
import sys
import itertools
import copy

def parse_in(std_in):
    cubes = {}
    for y, line in enumerate(std_in):
        for x, letter in enumerate(line):
            pos = (x, y, 0)
            if letter == '#':
                cubes[pos] = '#'
    return cubes

def expand_to_relevant(cubes, directions):
    start_pos = list(cubes)
    for pos in start_pos:
        if cubes[pos] == '#':
            for _dir in directions:
                new_pos = tuple(p+d for p, d in zip(pos, _dir))
                cubes[new_pos] = cubes.get(new_pos, '.')

def count_nearby(pos, cubes, directions):
    count = 0
    for _dir in directions:
        new_pos = tuple(p+d for p, d in zip(pos, _dir))
        if cubes.get(new_pos, '.') == '#':
            count += 1
    return count

def iterate(cubes, directions):
    expand_to_relevant(cubes, directions)
    new_cubes = {}
    for c in cubes:
        if cubes[c] == '#':
            if count_nearby(c, cubes, directions) in [2, 3]:
                new_cubes[c] = '#'
        if cubes[c] == '.':
            if count_nearby(c, cubes, directions) == 3:
                new_cubes[c] = '#'
    return new_cubes

def first_task(parsed_lines):
    directions = list(itertools.product([1, -1, 0], repeat=3))
    directions.remove((0,0,0))
    print(directions)
    cubes = copy.deepcopy(parsed_lines)
    print(cubes)
    for _ in range(6):
        cubes = iterate(cubes, directions)
    return len(cubes)

def second_task(parsed_lines):
    directions = list(itertools.product([1, -1, 0], repeat=4))
    directions.remove((0,0,0,0))
    cubes = {(x, y, z, 0) : '#' for x, y, z in parsed_lines}
    print(cubes)
    for _ in range(6):
        cubes = iterate(cubes, directions)
    return len(cubes)

def main():
    std_in = sys.stdin.readlines()

    parsed = parse_in(std_in)

    res = first_task(parsed)
    print(f"task 1: {res}")

    res = second_task(parsed)
    print(f"task 2: {res}")

if __name__ == "__main__":
    main()
