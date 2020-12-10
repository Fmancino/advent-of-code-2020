#!/usr/bin/env python3
import sys

def parse_in(std_in):
    return [int(i) for i in std_in]

def first_task(parsed):
    parsed.sort()
    parsed.insert(0, 0)
    diff_3 = 0
    diff_1 = 0
    for idx, val in enumerate(parsed):
        if idx == len(parsed) - 1:
            to_next = 3
        else:
            to_next = parsed[idx + 1] - val
        if to_next == 3:
            diff_3 += 1
        elif to_next == 1:
            diff_1 += 1
        elif to_next != 2:
            raise ValueError('bad input')
    return diff_1 * diff_3

def second_task(parsed, first_res):
    return 0

def main():
    std_in = sys.stdin.readlines()

    parsed = parse_in(std_in)

    res = first_task(parsed)
    print(f"task 1: {res}")

    res = second_task(parsed, res)
    print(f"task 2: {res}")

if __name__ == "__main__":
    main()
