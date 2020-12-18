#!/usr/bin/env python3
import sys

def parse_in(std_in):
    return [s.strip() for s in std_in]

def plus(a, b):
    return a + b

def times(a, b):
    return a * b

OPER_DICT = {'+': plus, '*': times}

def add_parens(text):
    _open = 1
    for idx, l in enumerate(text):
        if l == '(':
            _open += 1
        elif l == ')':
            _open -= 1
            if _open == 0:
                return '(' + text[:idx] + ')' + text[idx:]
    return '(' + text + ')'

def calculate(text):
    while True:
        if text[0] == '(':
            text = calculate(text[1:])
        space = text.find(' ')
        for idx, l in enumerate(text):
            if l == ' ':
                space = idx
                break
            elif l == ')':
                return text[:idx] + text[idx+1:]
            elif idx == len(text) - 1:
                return text
        first_num = int(text[:space])
        text = text[space+1:]
        operation = OPER_DICT[text[0]]
        text = text[2:]
        #Comment next 2 lines to get star 1
        if operation == times:
            text = add_parens(text)
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

def second_task(parsed_lines):
    _sum = 0
    for line in parsed_lines:
        _sum += int(calculate(line))
    return _sum

def main():
    std_in = sys.stdin.readlines()

    parsed = parse_in(std_in)

    #res = first_task(parsed)
    #print(f"task 1: {res}")

    res = second_task(parsed)
    print(f"task 2: {res}")

if __name__ == "__main__":
    main()
