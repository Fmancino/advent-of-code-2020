#!/usr/bin/env python3
import sys
import re


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

def is_valid(_pass):
    fields_no_cid = [('byr', byr_ver),
                     ('iyr', iyr_ver),
                     ('eyr', eyr_ver),
                     ('hgt', hgt_ver),
                     ('hcl', hcl_ver),
                     ('ecl', ecl_ver),
                     ('pid', pid_ver)]
    for key, fun in fields_no_cid:
        text = _pass.get(key)
        if text is None:
            #print(f'{f} not found')
            return False
        if not fun(text):
            return False
    return True


def parse_in(std_in):
    pass_str = std_in.split('\n\n')
    pass_str = map(lambda x: x.replace('\n', ' '), pass_str)
    return list(map(line_to_dict, pass_str))

def first_task(passes):
    count = 0
    for p in passes:
        if is_no_cid_valid(p):
            count += 1
    return count

def second_task(parsed_lines):
    count = 0
    for p in parsed_lines:
        if is_valid(p):
            count += 1

    return count

def pid_ver(text):
    reg = re.compile(r"^\d{9}$")
    obj = reg.match(text)
    if obj is None:
        return False
    return True

def ecl_ver(text):
    reg = re.compile(r"^(amb|blu|brn|gry|grn|hzl|oth)$")
    obj = reg.match(text)
    if obj is None:
        return False
    return True

def hcl_ver(text):
    reg = re.compile(r"^#[0-9a-f]{6}$")
    obj = reg.match(text)
    if obj is None:
        return False
    return True

def hgt_ver(text):
    reg = re.compile(r"^(\d+)(cm|in)$")
    obj = reg.match(text)
    if obj is None:
        return False
    higth = int(obj.group(1))
    unit = obj.group(2)
    if unit == 'cm':
        if 150 <= higth <= 193:
            return True
    if unit == 'in':
        if 59 <= higth <= 76:
            return True
    return False

def eyr_ver(text):
    i = int(text)
    if 2020 <= i <= 2030:
        return True
    return False

def iyr_ver(text):
    i = int(text)
    if 2010 <= i <= 2020:
        return True
    return False

def byr_ver(text):
    i = int(text)
    if 1920 <= i <= 2002:
        return True
    return False

def main():
    std_in = sys.stdin.read()

    parsed = parse_in(std_in)

    res = first_task(parsed)
    print(f"task 1: {res}")

    res = second_task(parsed)
    print(f"task 2: {res}")

if __name__ == "__main__":
    main()
