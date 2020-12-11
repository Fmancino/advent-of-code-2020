#!/usr/bin/env python3
import sys
import copy

def get_close(grid, x, y):
    close = []
    close += [grid[y][x-1]]
    close += [grid[y][x+1]]
    close += [grid[y-1][x]]
    close += [grid[y+1][x]]
    close += [grid[y+1][x+1]]
    close += [grid[y-1][x-1]]
    close += [grid[y+1][x-1]]
    close += [grid[y-1][x+1]]
    return close

def get_nr_close(grid, x, y):
    close = get_close(grid, x, y)
    occupied = [1 for o in close if o == '#']
    return sum(occupied)

def grid_parse_line(line):
    seats = ['.']
    for l in line:
        seats += [l]
    seats += ['.']
    return seats

def parse_in(std_in):
    parsed = [grid_parse_line(i.strip()) for i in std_in]
    only_floor = ['.' for _ in parsed[0]]
    parsed.insert(0, only_floor)
    parsed.append(only_floor)
    return parsed

def first_task(grid):
    grid, old_grid = iteration(grid)
    while grid != old_grid:
        grid, old_grid = iteration(grid)

    count = 0
    for line in grid:
        for seat in line:
            if seat == '#':
                count += 1
    return count


def iteration(grid):
    old_grid = copy.deepcopy(grid)
    for y, row in enumerate(old_grid):
        for x, seat in enumerate(row):
            if seat == '#':
                if get_nr_close(old_grid, x, y) >= 4:
                    grid[y][x] = 'L'
            elif seat == 'L':
                if get_nr_close(old_grid, x, y) == 0:
                    grid[y][x] = '#'
    return grid, old_grid

def second_task(parsed):
    return 0

def main():
    std_in = sys.stdin.readlines()

    parsed = parse_in(std_in)

    res = first_task(parsed)
    print(f"task 1: {res}")

    res = second_task(parsed)
    print(f"task 2: {res}")

if __name__ == "__main__":
    main()
