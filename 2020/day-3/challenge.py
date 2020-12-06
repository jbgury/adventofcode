#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import operator

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))


def count_tree((move_right, move_down), lines):
    position_r = 0
    nb_trees = 0
    for l in lines[::move_down]:
        if l[position_r] == '#':
            nb_trees += 1
        position_r += move_right
        position_r = position_r % len(l)
    return nb_trees


print("--- PART 1 ---")
slope = (3, 1)
l1 = count_tree(slope, lines)
print("Key = %s" % l1)

print("--- PART 2 ---")
slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))

result_list = map(lambda x: count_tree(x, lines), slopes)
print("values are : %s " % (','.join(map(str, result_list))))
print("Key to solve the puzzle is %s " % reduce(operator.mul, result_list))
