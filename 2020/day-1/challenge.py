#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

acc_list = {}
for l in lines:
    v = int(l)
    acc_list[v] = 2020 - v
    if acc_list[v] in acc_list.keys():
        print("Found %s and %s into the list, key = %s" %
              (v, acc_list[v], v * acc_list[v]))

values1 = map(int, lines)
values2 = {}
for v in values1:
    values2[v] = [y for y in values1 if y <= 2020 - v]

for v in values2.keys():
    for k in values2[v]:
        if (2020 - v - k) in [x for x in values2[v] if x != k]:
            z = 2020 - v - k
            print("%s, %s, %s : key = %s " % (v, k, z, v * k * z))
