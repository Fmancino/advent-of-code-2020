#!/usr/bin/env python3
import sys
import copy
from collections import deque

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
    res = {}
    last_key = 0
    for idx, key in enumerate(parsed):
        if res.get(key) is None:
            res[key] = deque([idx])
        else:
            res[key].append(idx)
        last_key =  key
        last_idx =  idx
    while True:
        if len(res[last_key]) == 2:
            prev_pos = res[last_key].popleft()
            key = res[last_key][0] - prev_pos
        else:
            key = 0
        last_idx += 1
        if res.get(key) is None:
            res[key] = deque([last_idx])
        else:
            res[key].append(last_idx)
        last_key = key
        if last_idx == 30000000-1:
            return last_key

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
