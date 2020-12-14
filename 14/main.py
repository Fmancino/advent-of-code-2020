#!/usr/bin/env python3
import sys
import re

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
                elif l =='1':
                    and_str +=  '1'
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
    return 0

def main():
    std_in = sys.stdin.readlines()

    parsed = parse_in(std_in)
    print(parsed)

    res = first_task(parsed)
    print(f"task 1: {res}")

    res = second_task(parsed)
    print(f"task 2: {res}")

if __name__ == "__main__":
    main()
