#!/usr/bin/env python3
import sys
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
def is_ticket_valid(ticket, rules):
    for nr in ticket:
        if not is_valid(nr, rules):
            return False
    return True

def get_matches(nr, rules):
    matches = []
    for key, r in rules.items():
        if in_range(nr, r[0]) or in_range(nr, r[1]):
            matches += [key]
    return matches

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

def in_each(element, lists):
    for l in lists:
        if element not in l:
            return False
    return True

def get_possible_placements(valid_tickets, rules):
    ''' temporary result, for each index give all possible rules that could fit '''
    matches_db = []
    for t in valid_tickets:
        t_matches = []
        for nr in t:
            t_matches.append(get_matches(nr, rules))
        matches_db.append(t_matches)
    res = {idx: [] for idx in range(len(rules))}
    for idx in range(len(rules)):
        ms_idx = [m[idx] for m in matches_db]
        for m in ms_idx[0]:
            if in_each(m, ms_idx[1:]):
                res[idx].append(m)
    return res

def second_task(parsed):
    rules = parsed[0]
    my_ticket = parsed[1]
    near_tickets = parsed[2]
    valid_tickets = [t for t in near_tickets if is_ticket_valid(t, rules)]
    valid_tickets += [my_ticket]
    res = get_possible_placements(valid_tickets, rules)
    done = {}
    while True:
        # clean up, make sure we get one rule per each index
        for idx, r in res.items():
            if len(r) == 1:
                val = res.pop(idx)[0]
                done[idx] = val
                break
        for idx, r in res.items():
            try:
                r.remove(val)
            except ValueError:
                pass
        if not res:
            break
    #print(done)
    departure_idx = [idx for idx in done if done[idx].startswith('departure')]
    mult = 1
    for i in departure_idx:
        mult *= my_ticket[i]
    return mult

def main():
    std_in = sys.stdin.read()

    parsed = parse_in(std_in)

    res = first_task(parsed)
    print(f"task 1: {res}")

    res = second_task(parsed)
    print(f"task 2: {res}")

if __name__ == "__main__":
    main()
