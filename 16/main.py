#!/usr/bin/env python3
import sys
import copy
import re

def parse_in(std_in):
    vec = std_in.split('\n\n')
    rules_str = vec[0].splitlines()
    my_ticket_str = vec[1].splitlines()
    all_tickets_str = vec[2].splitlines()
    my_ticket = [int(i) for i in my_ticket_str[1].split(',')]
    rule_re = re.compile(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)')
    rules = {}
    for line in rules_str:
        obj = rule_re.match(line)
        rules[obj.group(1)] = ((int(obj.group(2)), int(obj.group(3))),
                               (int(obj.group(4)), int(obj.group(5))))
    all_tickets = []
    for line in all_tickets_str[1:]:
        all_tickets.append([int(i) for i in line.split(',')])
    return rules, my_ticket, all_tickets

def is_valid(nr, rules):
    valid = False
    for r in rules.values():
        if in_range(nr, r[0]) or in_range(nr, r[1]):
            valid = True
            break
    return valid

def in_range(val, rng):
    return rng[0] <= val <= rng[1]

def first_task(parsed):
    rules = parsed[0]
    all_tickets = parsed[2]
    count = 0
    for t in all_tickets:
        for nr in t:
            if not is_valid(nr, rules):
                count += nr
    return count

def second_task(parsed):
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
