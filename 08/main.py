#!/usr/bin/env python3
import sys
import re
import time
import copy

RE_ACC = re.compile(r'acc ([+-]\d+)')
RE_JMP = re.compile(r'jmp ([+-]\d+)')
RE_NOP = re.compile(r'nop ([+-]\d+)')

def parse_line(text):
    obj = RE_ACC.match(text)
    if obj is not None:
        return ('acc', int(obj.group(1)))
    obj = RE_JMP.match(text)
    if obj is not None:
        return ('jmp', int(obj.group(1)))
    obj = RE_NOP.match(text)
    if obj is not None:
        return ('nop', int(obj.group(1)))
    raise ValueError('Bad line provided')


def first_task(parsed_lines):
    seen = {}
    accumulator = 0
    line_nr = 0
    while seen.get(line_nr) is None:
        instr = parse_line(parsed_lines[line_nr])
        seen[line_nr] = instr
        cmd = instr[0]
        nr = instr[1]
        if cmd == 'acc':
            accumulator += nr
            line_nr += 1
        elif cmd == 'jmp':
            line_nr += nr
        else:
            line_nr += 1
        if line_nr >= len(parsed_lines):
            return accumulator, True
    return accumulator, False

def fix_line(parsed_lines, line_nr):
    line = parsed_lines[line_nr]
    if line.startswith('jmp'):
        line = 'nop' + line[3:]
    else:
        line = 'jmp' + line[3:]
    parsed_lines[line_nr] = line

def second_task(parsed_lines):
    for line_nr, line in enumerate(parsed_lines):
        if line.startswith('acc'):
            continue
        tmp = copy.deepcopy(parsed_lines)
        fix_line(tmp, line_nr)
        acc, is_done = first_task(tmp)
        if is_done:
            return acc
    raise ValueError('fucked up')

def main():
    std_in = sys.stdin.readlines()

    parsed = std_in#parse_in(std_in)

    res = first_task(parsed)
    print(f"task 1: {res}")

    res = second_task(parsed)
    print(f"task 2: {res}")

def lower(rng):
    _len = rng[1] - rng[0] + 1
    return (rng[0], (rng[0] + _len // 2 - 1))

def upper(rng):
    _len = rng[1] - rng[0] + 1
    return ((rng[0] + _len // 2), rng[1])

if __name__ == "__main__":
    main()
