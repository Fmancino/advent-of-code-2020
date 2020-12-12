#!/usr/bin/env python3
import sys
import copy
import numpy as np
import math

class Ship():

    x = 0
    y = 0

    def __init__(self):
        self.facing_nr = 0
        self.dire = "ENWS"
        self.nr_dir = len(self.dire)

    def execute_instruction(self, inst):
        cmd = inst[0]
        nr = inst[1]
        if cmd == "N":
            self.y += nr
        elif cmd == "S":
            self.y -= nr
        elif cmd == "E":
            self.x += nr
        elif cmd == "W":
            self.x -= nr
        elif cmd == "L":
            jump = nr // 90
            self.facing_nr = (self.facing_nr + jump) % self.nr_dir
        elif cmd == "R":
            jump = nr // 90
            self.facing_nr = (self.facing_nr - jump) % self.nr_dir
        elif cmd == "F":
            self.execute_instruction((self.dire[self.facing_nr], nr))

    def get_distance(self):
        return abs(self.x) + abs(self.y)

class Ship2(Ship):

    left_90_rotation = [ [1, 0]]

    def __init__(self):
        self.w_x = 10
        self.w_y = 1

    def execute_instruction(self, inst):
        cmd = inst[0]
        nr = inst[1]
        if cmd == "N":
            self.w_y += nr
        elif cmd == "S":
            self.w_y -= nr
        elif cmd == "E":
            self.w_x += nr
        elif cmd == "W":
            self.w_x -= nr
        elif cmd == "L":
            rot_mat = get_rotation_matrix(nr)
            (self.w_x, self.w_y) = np.dot(rot_mat, (self.w_x, self.w_y))
        elif cmd == "R":
            rot_mat = get_rotation_matrix(-nr)
            (self.w_x, self.w_y) = np.dot(rot_mat, (self.w_x, self.w_y))
        elif cmd == "F":
            self.x += self.w_x * nr
            self.y += self.w_y * nr


def get_rotation_matrix(degrees):
    """ counterclockwise rotation matrix """
    r = math.radians(degrees)
    rot_mat = ([int(math.cos(r)), -int(math.sin(r))],
               [int(math.sin(r)), int(math.cos(r))])
    return rot_mat


def parse_in(std_in):
    ret = [l.strip() for l in std_in]
    ret = [(l[0], int(l[1:])) for l in ret]
    return ret

def first_task(parsed):
    s = Ship()
    for i in parsed:
        s.execute_instruction(i)
    return s.get_distance()

def second_task(parsed):
    s = Ship2()
    for i in parsed:
        s.execute_instruction(i)
    return s.get_distance()

def main():
    std_in = sys.stdin.readlines()

    parsed = parse_in(std_in)

    res = first_task(parsed)
    print(f"task 1: {res}")

    res = second_task(copy.deepcopy(parsed))
    print(f"task 2: {res}")

if __name__ == "__main__":
    main()
