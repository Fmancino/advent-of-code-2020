#!/usr/bin/env python3
import sys
import copy

def parse_in(std_in):
    ret = std_in.strip().split(',')
    ret = [int(i) for i in ret]
    return ret

def first_task(parsed):
    res = copy.deepcopy(parsed)
    while True:
        res += [-reverse_find(res[:-1], res[-1])]
        if len(res) == 2020:
            break
    return res[-1]

def second_task(parsed):
    return 0

def reverse_find(_list, val):
    for i in range(-1, -len(_list) - 1, -1):
        if val == _list[i]:
            return i
    return 0



def main():
    std_in = sys.stdin.read()

    parsed = parse_in(std_in)

    res = first_task(parsed)
    print(f"task 1: {res}")

    res = second_task(parsed)
    print(f"task 2: {res}")

if __name__ == "__main__":
    main()
