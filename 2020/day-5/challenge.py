#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re

records = [l.rstrip('\n') for l in sys.stdin]
low = ['F', 'L']
max_row = 128
max_column = 8
pattern = re.compile("(?P<row>[FB]*)(?P<column>[LR]*)")

print("--- Warm-up ---")

sample = ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']


def binary_search(instruction, sequence):
    if instruction[0] in low:
        part = sequence[:len(sequence) // 2]
    else:
        part = sequence[len(sequence) // 2:]

    if len(instruction) == 1:
        if instruction[0] in low:
            return sequence[0]
        else:
            return sequence[1]
    elif len(instruction) == 1 and len(sequence) > 2:
        print(
            "Issue with the instruction , sequence is %s, instruction is %s" %
            (sequence, instruction))
    else:
        return binary_search(instruction[1:], part)


for s in sample:
    m = pattern.match(s)
    print("For sample %s, row = %s, column = %s" %
          (s, binary_search(m.group('row'), list(range(
              0, 128))), binary_search(m.group('column'), list(range(0, 8)))))

print("--- Part 1 ---")
list_seat_id = []
for l in records:
    m = pattern.match(l)
    r = binary_search(m.group('row'), list(range(0, 128)))
    c = binary_search(m.group('column'), list(range(0, 8)))
    list_seat_id.append(r * 8 + c)

list_seat_id.sort()
list_seat_id.reverse()
max_seat_id = list_seat_id[0]
print(max_seat_id)

print("--- PART 2 ---")

list_seat_id.reverse()
full_list = range(0, max_seat_id)
missing_seat_id = [
    s for s in full_list if s not in list_seat_id and s +
    1 in list_seat_id and s - 1 in list_seat_id
]

print(missing_seat_id)
