#!/usr/bin/env python3
import sys
import itertools
import copy

def parse_in(std_in):
    return [s.strip() for s in std_in]


def plus(a, b):
    return a + b

def times(a, b):
    return a * b

OPER_DICT = {'+': plus, '*': times}

def calculate(text):
    while True:
        if text[0] == '(':
            text = calculate(text[1:])
        space = text.find(' ')
        if space > 0:
            first_num = int(text[:space])
            text = text[space+1:]
        else:
            raise ValueError
        operation = OPER_DICT[text[0]]
        text = text[2:]
        if text[0] == '(':
            text = calculate(text[1:])
        for idx, l in enumerate(text):
            if l == ' ':
                fin = idx
                break
            elif l == ')':
                fin = idx
                next_num = int(text[:fin])
                res = operation(first_num, next_num)
                return str(res) + text[fin+1:]
            elif idx == len(text) - 1:
                next_num = int(text)
                res = operation(first_num, next_num)
                return str(res)
        next_num = int(text[:fin])
        text = text[fin:]
        res = operation(first_num, next_num)
        text = str(res) + text

def first_task(parsed_lines):
    _sum = 0
    for line in parsed_lines:
        _sum += int(calculate(line))
    return _sum

def second_task(parsed_lines):
    return 0

def main():
    std_in = sys.stdin.readlines()

    parsed = parse_in(std_in)

    res = first_task(parsed)
    print(f"task 1: {res}")

    res = second_task(parsed)
    print(f"task 2: {res}")

if __name__ == "__main__":
    main()
