#!/usr/bin/env python3
import sys

def first_task(in_num, to_sum=2020):
    for idx, val in enumerate(in_num):
        to_2020 = to_sum - val
        if to_2020 in in_num[idx+1:]:
            return True, val, to_2020
    return False, 0, 0

def second_task(in_num):
    for idx, val in enumerate(in_num):
        to_2020 = 2020 - val
        res, val1, val2 = first_task(in_num[:val] + in_num[val+1:], to_2020)
        if res:
            return True, val1, val2, val
    return False, 0, 0, 0

def main():
    std_in = sys.stdin.readlines()
    in_num = []

    for i in std_in:
        in_num.append(int(i))

    _, val1, val2 = first_task(in_num)
    mult = val1 * val2
    print(f"task 1: {mult}")

    _, val1, val2, val3 = second_task(in_num)
    mult = val1 * val2 * val3
    print(f"task 2: {mult}")

if __name__ == "__main__":
    main()
