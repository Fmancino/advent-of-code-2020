#!/usr/bin/env python3
import sys
import re

def parse_in(std_in):
    line_re = re.compile(r"(\d+)-(\d+) (.): (.+)")
    parsed_lines = []
    for i in std_in:
        obj = line_re.match(i)
        _min = int(obj.group(1))
        _max = int(obj.group(2))
        letter = obj.group(3)
        text = obj.group(4)
        parsed_lines.append((_min, _max, letter, text))
    return parsed_lines

def first_task(parsed_lines):
    count = 0
    for (_min, _max, letter, text) in parsed_lines:
        if is_valid(_min, _max, letter, text):
            count += 1
    return count

def second_task(parsed_lines):
    count = 0
    for (_min, _max, letter, text) in parsed_lines:
        if second_valid(_min, _max, letter, text):
            count += 1
    return count

def is_valid(_min, _max, letter, text):
    count = 0
    for l in text:
        if l == letter:
            count += 1
    return _min <= count <= _max

def second_valid(_min, _max, letter, text):
    # exclusive or
    return (text[_min - 1] == letter) != (text[_max - 1] == letter)

def main():
    std_in = sys.stdin.readlines()

    lines = parse_in(std_in)

    count = first_task(lines)
    print(f"task 1: {count}")

    count = second_task(lines)
    print(f"task 2: {count}")

if __name__ == "__main__":
    main()
