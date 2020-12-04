#!/usr/bin/env python3
import sys

fields = ['byr',
          'iyr',
          'eyr',
          'hgt',
          'hcl',
          'ecl',
          'pid',
          'cid']


def line_to_dict(line):
    _list = line.split(' ')
    _dict = {}
    for l in _list:
        keyval = l.split(':')
        if len(keyval) == 2:
            key = keyval[0]
            val = keyval[1]
            _dict[key] = val
    return _dict

def is_no_cid_valid(_pass):
    fields_no_cid = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for f in fields_no_cid:
        if _pass.get(f) is None:
            #print(f'{f} not found')
            return False
    return True


def parse_in(std_in):
    pass_str = std_in.split('\n\n')
    pass_str = map(lambda x: x.replace('\n', ' '), pass_str)
    return map(line_to_dict, pass_str)

def first_task(passes):
    count = 0
    for p in passes:
        if is_no_cid_valid(p):
            count += 1
    return count

def second_task(parsed_lines):
    mult = 1
    return mult

def main():
    std_in = sys.stdin.read()

    parsed = parse_in(std_in)

    res = first_task(parsed)
    print(f"task 1: {res}")

    #  res = second_task(parsed_lines)
    #  print(f"task 2: {res}")

if __name__ == "__main__":
    main()
