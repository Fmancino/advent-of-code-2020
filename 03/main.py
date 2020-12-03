#!/usr/bin/env python3
import sys
from collections import namedtuple

Point = namedtuple('Point', 'x y')

def parse_in(std_in):
    parsed_lines = []
    for line in std_in:
        data_line = []
        for letter in line:
            if letter in "#.":
                data_line.append(letter)
        parsed_lines.append(data_line)
    return parsed_lines

def _next(point, delta, max_y):
    x = point.x + delta.x
    y = point.y + delta.y
    y %= max_y
    return Point(x, y)

def is_tree(point, parsed_lines):
    return parsed_lines[point.x][point.y] == '#'

def first_task(parsed_lines, delta):
    delta = Point(*delta)
    count = 0
    point = Point(0, 0)
    max_y = len(parsed_lines[0])
    max_x = len(parsed_lines)
    count = 0
    while point.x != max_x - 1:
        point = _next(point, delta, max_y)
        if is_tree(point, parsed_lines):
            count += 1
    return count

def second_task(parsed_lines):
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    num = []
    mult = 1
    for s in slopes:
        c = first_task(parsed_lines, s)
        num.append(c)
        mult *= c
    print(num)
    return mult

def main():
    std_in = sys.stdin.readlines()

    parsed_lines = parse_in(std_in)

    res = first_task(parsed_lines, (1, 3))
    print(f"task 1: {res}")

    res = second_task(parsed_lines)
    print(f"task 2: {res}")

if __name__ == "__main__":
    main()
