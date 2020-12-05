#!/usr/bin/env python3
import sys
import re

def parse_in(std_in):
    row_rng = (0, 127)
    col_rng = (0, 7)
    seats = []
    for line in std_in:
        row = iterate(row_rng, line[:7], 'F', 'B')
        col = iterate(col_rng, line[7:10], 'L', 'R')
        seats.append(Seat(row, col))
    return seats

def iterate(rng, commands, low_char, upp_char):
    for c in commands:
        if c == low_char:
            rng = lower(rng)
        elif c == upp_char:
            rng = upper(rng)
        else:
            raise ValueError(f'Character {c} not recognized')
    if rng[0] != rng[1]:
        raise ValueError(f'Iteration not finished')
    return rng[0]

def first_task(parsed_lines):
    _max = max([s.id for s in parsed_lines])
    return _max

class Seat:
    """ Keep track of seats """

    def __init__(self, row=None, col=None, _id=None):
        if _id is not None:
            self.row = _id // 8
            self.col = _id % 8
            self.id = _id
        else:
            self.row = row
            self.col = col
            self.id = self.row * 8 + self.col

    def __eq__(self, other):
        return self.id == other.id

    def taken(self, taken_seats):
        if self in taken_seats:
            return True
        if (self + 1 in taken_seats and self - 1 in taken_seats):
            return False
        return True

    def __int__(self):
        return self.id

    def __add__(self, other):
        return Seat(_id=int(self)+int(other))

    def __sub__(self, other):
        return Seat(_id=int(self)-int(other))

def second_task(parsed_lines):
    my_seat = Seat(0,0)
    while True:
        if my_seat.taken(parsed_lines):
            my_seat += 1
        else:
            break
        if my_seat.id > 9999:
            raise ValueError(f'Error: {my_seat.row}, {my_seat.col}')
    return my_seat.id

def main():
    std_in = sys.stdin.readlines()

    parsed = parse_in(std_in)

    res = first_task(parsed)
    print(f"task 1: {res}")

    res = second_task(parsed)
    print(f"task 2: {res}")

def lower(rng):
    _len = rng[1] - rng[0] + 1
    return (rng[0], (rng[0] + _len // 2 - 1))

def upper(rng):
    _len = rng[1] - rng[0] + 1
    return ((rng[0] + _len // 2), rng[1])

if __name__ == "__main__":
    main()
