#!/usr/bin/env python3
import sys

def sum_to_nr(in_num, result):
    for idx, val in enumerate(in_num):
        missing = result - val
        if missing in in_num[idx+1:]:
            return True, val, missing
    return False, 0, 0

def parse_in(std_in):
    return [int(i) for i in std_in]

def first_task(parsed):
    #nr_before = 5
    nr_before = 25
    idx = nr_before
    for i in parsed[nr_before:]:
        is_valid, _, _ = sum_to_nr(parsed[idx-nr_before:idx], i)
        if not is_valid:
            return i
        idx += 1
    raise ValueError('bad input')

def second_task(parsed, first_res):
    lwr_idx = 0
    upp_idx = 2
    while upp_idx < len(parsed):
        rng = parsed[lwr_idx:upp_idx]
        sum_rng = sum(rng)
        if sum_rng < first_res:
            upp_idx += 1
        elif sum_rng == first_res:
            return min(rng) + max (rng)
        else:
            lwr_idx += 1
            if lwr_idx == upp_idx - 1:
                upp_idx += 1
    raise ValueError('bad input')

def main():
    std_in = sys.stdin.readlines()

    parsed = parse_in(std_in)

    res = first_task(parsed)
    print(f"task 1: {res}")

    res = second_task(parsed, res)
    print(f"task 2: {res}")

if __name__ == "__main__":
    main()
