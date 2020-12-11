#!/usr/bin/env python3
import sys
import copy

def get_close(grid, x, y):
    close = 0
    close += grid[y][x-1] == '#'
    close += grid[y][x+1] == '#'
    close += grid[y-1][x] == '#'
    close += grid[y+1][x] == '#'
    close += grid[y+1][x+1] == '#'
    close += grid[y-1][x-1] == '#'
    close += grid[y+1][x-1] == '#'
    close += grid[y-1][x+1] == '#'
    return close

def hit_occupied(grid, start, trajectory):
    x = start[0]
    y = start[1]
    xt = trajectory[0]
    yt = trajectory[1]
    while True:
        x += xt
        y += yt
        if y < 0 or x < 0:
            return 0
        try:
            _next = grid[y][x]
        except IndexError:
            return 0
        if _next == "L":
            return 0
        if _next == "#":
            return 1

def get_close_2(grid, x, y):
    count = 0
    trajectories = [(1, 0),
                    (0, 1),
                    (-1, 0),
                    (0, -1),
                    (1, 1),
                    (-1, -1),
                    (-1, 1),
                    (1, -1)]
    for t in trajectories:
        count += hit_occupied(grid, (x, y), t)
    return count

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
                if get_close(old_grid, x, y) >= 4:
                    grid[y][x] = 'L'
            elif seat == 'L':
                if get_close(old_grid, x, y) == 0:
                    grid[y][x] = '#'
    return grid, old_grid

def iteration2(grid):
    old_grid = copy.deepcopy(grid)
    for y, row in enumerate(old_grid):
        for x, seat in enumerate(row):
            if seat == '#':
                if get_close_2(old_grid, x, y) >= 5:
                    grid[y][x] = 'L'
            elif seat == 'L':
                if get_close_2(old_grid, x, y) == 0:
                    grid[y][x] = '#'
    return grid, old_grid

def print_grid(grid):
    for line in grid:
        l = ""
        for letter in line:
            l += letter
        print(l)
    print()

def second_task(parsed):
    grid, old_grid = iteration2(parsed)
    #print_grid(grid)
    while grid != old_grid:
        grid, old_grid = iteration2(grid)
        #print_grid(grid)

    #print_grid(grid)
    count = 0
    for line in grid:
        for seat in line:
            if seat == '#':
                count += 1
    return count

def main():
    std_in = sys.stdin.readlines()

    parsed = parse_in(std_in)

    res = first_task(copy.deepcopy(parsed))
    print(f"task 1: {res}")

    res = second_task(copy.deepcopy(parsed))
    print(f"task 2: {res}")

if __name__ == "__main__":
    main()
