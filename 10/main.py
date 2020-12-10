#!/usr/bin/env python3
import sys
from itertools import permutations

def parse_in(std_in):
    parsed = [int(i) for i in std_in]
    parsed.sort()
    parsed.insert(0, 0)
    parsed.append(max(parsed) + 3)
    return parsed

def first_task(parsed):
    diff_3 = 0
    diff_1 = 0
    for idx, val in enumerate(parsed[0:-1]):
        to_next = parsed[idx + 1] - val
        if to_next == 3:
            diff_3 += 1
        elif to_next == 1:
            diff_1 += 1
        elif to_next != 2:
            raise ValueError('bad input')
    print(len(parsed))
    print(diff_3)
    return diff_1 * diff_3

def is_valid(perm):
    for idx, val in enumerate(perm[0:-1]):
        to_next = perm[idx + 1] - val
        if to_next not in [1,2,3]:
            return False
    return True

def second_task(parsed):
    smaller = []
    last_idx = 0
    for idx, val in enumerate(parsed[0:-1]):
        to_next = parsed[idx + 1] - val
        if to_next == 3:
            smaller.append(parsed[last_idx:idx+1])
            last_idx = idx + 1
    valid_perms = []
    for s in smaller:
        valid_perm = 0
        if len(s) in [1,2]:
            # one is not interesting
            continue
        all_perm = []
        internal = s[1:-1]
        all_perm.append(())
        for i in range(1, len(internal)+1):
            all_perm += list(permutations(internal, i))
        for p in all_perm:
            p = list(p)
            p.append(s[-1])
            p.insert( 0, s[0])
            if is_valid(p):
                valid_perm += 1
        valid_perms.append(valid_perm)
    mult = 1
    for p in valid_perms:
        mult *= p
    return mult

def main():
    std_in = sys.stdin.readlines()

    parsed = parse_in(std_in)

    res = first_task(parsed)
    print(f"task 1: {res}")

    res = second_task(parsed)
    print(f"task 2: {res}")

if __name__ == "__main__":
    main()
