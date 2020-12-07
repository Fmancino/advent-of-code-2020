#!/usr/bin/env python3
import sys
import re
from collections import namedtuple

Baglink = namedtuple('Baglink', 'count bag')

class Bag:
    def __init__(self, color_str):
        self.color = color_str
        self.contains = []
        self.is_contained = []
        self.hash = hash(self.color)

    def __eq__(self, other):
        return self.color == str(other)

    def __hash__(self):
        return self.hash

    def __str__(self):
        return self.color

    def __repr__(self):
        return str(self)

    def full_repr(self):
        return f'\n{self.color}\nContains: {self.contains}\nIs contained: {self.is_contained}\n'

    def full_is_contained(self):
        con = []
        for c in self.is_contained:
            con.append(c)
            con += c.full_is_contained()
        return con

    def nr_contained(self):
        count = 0
        for c in self.contains:
            count += c[0] * (c[1].nr_contained() + 1 )
        return count

def parse_content(con, bags):
    if con.startswith('no'):
        return []
    con = con[:-1] #remove ending dot
    con = con.split(', ')
    line_re = re.compile(r"(\d+) (.+)")
    ret = []
    for c in con:
        obj = line_re.match(c)
        count = int(obj.group(1))
        bag_str = obj.group(2)
        if (count == 1):
            bag_str += 's'
        bag = bags[bag_str]
        ret.append((count, bag))
    return ret


def parse_in(std_in):
    temp = [x.rstrip().split(' contain ') for x in std_in]
    bags = {}
    for t in temp:
        bag = Bag(t[0])
        bags[t[0]] = bag
    #print (bags)
    for t in temp:
        b = bags[t[0]]
        b.contains = parse_content(t[1], bags)
        for c in b.contains:
            bags[c[1]].is_contained.append(b)
    return bags

def first_task(parsed):
    return len(set(parsed['shiny gold bags'].full_is_contained()))

def second_task(parsed):
    return parsed['shiny gold bags'].nr_contained()

def main():
    std_in = sys.stdin.readlines()

    parsed = parse_in(std_in)

    res = first_task(parsed)
    print(f"task 1: {res}")

    res = second_task(parsed)
    print(f"task 2: {res}")

if __name__ == "__main__":
    main()
