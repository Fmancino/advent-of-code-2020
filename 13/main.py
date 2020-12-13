#!/usr/bin/env python3
import sys
import copy
sys.path.append('../utils')
import crypto

def parse_in(std_in):
    parsed = [i.strip() for i in std_in]
    time = int(parsed[0])
    busses = parsed[1].split(',')
    busses_dict = {}
    for idx, b in enumerate(busses):
        if b != 'x':
            busses_dict[idx] = int(b)
    return time, busses_dict

def first_task(parsed):
    time = parsed[0]
    busses = parsed[1]
    to_bus = map(lambda b: (b, b - (time % b)), busses.values())
    smallest = min(to_bus, key=lambda x:x[1])
    return smallest[1] * smallest[0]

def second_task(parsed):
    busses = parsed[1]
    rests = []
    vals = []
    for key, val in busses.items():
        rests += [(val - key) % val] # key has to be 'inverted'
        vals += [val]
    # Solution after google helps
    num = crypto.chinese_remainder_gauss(vals, rests)

    # Slow solution (toooooo slow)
    #idx = 1
    #big_key = max(busses, key=busses.get)
    #while True:
    #    time = (idx * busses[big_key]) - big_key
    #    found = True
    #    for key, val in busses.items():
    #        if (time + key) % val != 0:
    #            found = False
    #            break
    #    if found:
    #        break
    #    idx += 1

    return num

def main():
    std_in = sys.stdin.readlines()

    parsed = parse_in(std_in)

    res = first_task(copy.deepcopy(parsed))
    print(f"task 1: {res}")

    res = second_task(copy.deepcopy(parsed))
    print(f"task 2: {res}")

if __name__ == "__main__":
    main()
