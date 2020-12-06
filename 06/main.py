#!/usr/bin/env python3
import sys
import re
from string import ascii_lowercase


def parse_in(std_in):
    res = std_in.split('\n\n')
    res = map(lambda x: x.rstrip(), res)
    return list(res)

def first_task(parsed):
    count = 0
    for p in parsed:
        for l in ascii_lowercase:
            if l in p:
                count += 1
    return count

def second_task(parsed):
    count = 0
    list_all_yes = []
    for group in parsed:
        persons = group.split('\n')
        all_yes = ''
        first = persons[0]
        for letter in first:
            l_all_yes = True
            for no_first in persons[1:]:
                if letter not in no_first:
                    l_all_yes = False
                    break
            if l_all_yes:
                all_yes += letter
        #print(f'{all_yes}')
        list_all_yes.append(all_yes)
    return first_task(list_all_yes)

def main():
    std_in = sys.stdin.read()

    parsed = parse_in(std_in)

    res = first_task(parsed)
    print(f"task 1: {res}")

    res = second_task(parsed)
    print(f"task 2: {res}")

if __name__ == "__main__":
    main()
