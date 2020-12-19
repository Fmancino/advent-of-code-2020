#!/usr/bin/env python3
import sys
import itertools
import copy
import datetime

def parse_in(std_in):
    res = std_in.split('\n\n')
    rules = res[0].splitlines()
    rules = [r.split(': ') for r in rules]
    rules = {int(r[0]): r[1].strip().split(' | ') for r in rules}
    for r in rules:
        rules[r] = [i.split(' ') for i in rules[r]]
    for r in rules.values():
        for g_idx in range(len(r)):
            try:
                r[g_idx] = [int(i) for i in r[g_idx]]
            except:
                pass
    strings = res[1].splitlines()
    strings = [r.strip() for r in strings]
    return rules, strings

def parse_rule(rule_idx, rules):
    rule = rules[rule_idx]
    if type(rule[0]) == str:
        return rule
    done = []
    for g in rule:
        prev = False
        for r in g:
            if r == '"a"':
                return ["a"]
            if r == '"b"':
                return ["b"]
            r = parse_rule(r, rules)
            if prev:
                r = [i[0] + i[1] for i in itertools.product(prev,r)]
            prev = r
        done += prev
    rules[rule_idx] = done
    return done


def first_task(parsed_lines):
    rules = parsed_lines[0]
    strings = parsed_lines[1]
    parsed_rule = parse_rule(0, rules)
    return sum([s in parsed_rule for s in strings])

def second_task(parsed_lines):
    rules = parsed_lines[0]
    strings = parsed_lines[1]
    rules[0] = [[8], [11]]
    rules[8] = [[42],[42, 8]]
    rules[11] = [[42, 31],[42, 11, 31]]
    rule42 = parse_rule(42, rules)
    rule31 = parse_rule(31, rules)
    print(rule42)
    print(rule31)
    return 0

def main():
    std_in = sys.stdin.read()

    parsed = parse_in(std_in)

    res = first_task(parsed)
    print(f"task 1: {res}")
    print(datetime.datetime.now())

    res = second_task(parsed)
    print(f"task 2: {res}")

if __name__ == "__main__":
    main()
