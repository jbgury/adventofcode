#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

import re

print("--- PART 1 ---")

pattern = re.compile(
    r"""
    (?P<minPolicy>\d+)
    -
    (?P<maxPolicy>\d+)
    [ ]*
    (?P<pattern>[^:]*)
    :[ ]*
    (?P<password>.*)
""", re.VERBOSE)

result = {"OK": [], "NOK": []}
for l in lines:
    m = pattern.match(l)
    list_pattern = [p for p in m.group("password") if p == m.group("pattern")]
    if len(list_pattern) >= int(
            m.group("minPolicy")) and len(list_pattern) <= int(
                m.group("maxPolicy")):
        result["OK"].append(m.groupdict())
    else:
        result["NOK"].append(m.groupdict())

print("Valid password number :", len(result["OK"]))

print("--- PART 2 ---")

result = {"OK": [], "NOK": []}
for l in lines:
    m = pattern.match(l)
    pos_1 = int(m.group("minPolicy"))
    pos_2 = int(m.group("maxPolicy"))
    if pos_1 >= len(m.group("password")):
        car_pos_1 = None
    else:
        car_pos_1 = m.group("password")[pos_1 - 1]
    if pos_2 > len(m.group("password")):
        car_pos_2 = None
    else:
        car_pos_2 = m.group("password")[pos_2 - 1]
    if car_pos_1 != car_pos_2 and (car_pos_1 == m.group("pattern") or \
                                   car_pos_2 == m.group("pattern")):
        result["OK"].append(m.groupdict())
    else:
        result["NOK"].append(m.groupdict())

print("Valid password number :", len(result["OK"]))
