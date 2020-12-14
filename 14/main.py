#!/usr/bin/env python3
import sys
import re
from collections import Counter

def parse_in(std_in):
    ret = [l.strip().split(' = ') for l in std_in]
    return ret

def first_task(parsed):
    mem = {}
    mem_re = re.compile(r'mem\[(\d+)\]')
    for name, number in parsed:
        if name == 'mask':
            or_str = ''
            and_str = ''
            for l in number:
                if l == 'X':
                    and_str += '1'
                    or_str += '0'
                elif l == '1':
                    and_str += '1'
                    or_str += '1'
                elif l == '0':
                    and_str += '0'
                    or_str += '0'
                else:
                    raise ValueError('parsing error')
            or_nr = int(or_str, 2)
            and_nr = int(and_str, 2)
        elif name.startswith('mem'):
            obj = mem_re.match(name)
            addr = obj.group(1)
            mem[addr] = int(number) & and_nr | or_nr
    return sum(mem.values())

def second_task(parsed):
    mem = {}
    mem_re = re.compile(r'mem\[(\d+)\]')
    for name, number in parsed:
        if name == 'mask':
            and_nrs, or_nrs = fuzzy_mask(number)
        elif name.startswith('mem'):
            obj = mem_re.match(name)
            addr = int(obj.group(1))
            number = int(number)
            _sum = 0
            for and_nr, or_nr in zip(and_nrs, or_nrs):
                nr = addr & and_nr | or_nr
                mem[nr] = number
    return sum(mem.values())

def fuzzy_mask(mask_str):
    nr_of_x = Counter(mask_str)['X']
    fuzzy_strs = [f'{b:b}'.zfill(nr_of_x) for b in range(0, pow(2, nr_of_x))]
    and_nrs = []
    or_nrs = []
    for fuz in fuzzy_strs:
        or_str = ''
        and_str = ''
        for l in mask_str:
            if l == 'X':
                # Change to 1 or 0
                and_str += fuz[0]
                or_str += fuz[0]
                fuz = fuz[1:]
            elif l == '1':
                # Change to one
                and_str += '1'
                or_str += '1'
            elif l == '0':
                # unchanged
                and_str += '1'
                or_str += '0'
            else:
                raise ValueError('parsing error')
        or_nrs += [int(or_str, 2)]
        and_nrs += [int(and_str, 2)]
    return and_nrs, or_nrs

def main():
    std_in = sys.stdin.readlines()

    parsed = parse_in(std_in)

    res = first_task(parsed)
    print(f"task 1: {res}")

    res = second_task(parsed)
    print(f"task 2: {res}")

if __name__ == "__main__":
    main()
