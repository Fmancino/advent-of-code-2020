#!/usr/bin/env python3
""" Alternative solution with interesting tricks from other answers """
import sys
# Counter can count the number of occurrences of each letter in string
from collections import Counter

def parse_in(std_in):
    res = std_in.split('\n\n')
    res = [x.rstrip() for x in res]
    return res

def first_task(parsed):
    # the set trick, set will give you only one occurrence of each element
    res = [len(set(p.replace('\n', ''))) for p in parsed]
    return sum(res)

def second_task(parsed):
    count = 0
    for group in parsed:
        nr_persons = len(group.split('\n'))
        for v in Counter(group).values():
            if v == nr_persons:
                count += 1
    return count

def main():
    std_in = sys.stdin.read()

    parsed = parse_in(std_in)

    res = first_task(parsed)
    print(f"task 1: {res}")

    res = second_task(parsed)
    print(f"task 2: {res}")

if __name__ == "__main__":
    main()
