#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import functools
import operator
import itertools

records = [l.rstrip('\n') for l in sys.stdin]

print("--- WARMUP ---")

samples = [
    'abc',
    '',
    'a',
    'b',
    'c',
    '',
    'ab',
    'ac',
    '',
    'a',
    'a',
    'a',
    'a',
    '',
    'b',
]


def group_records(records, verbose=False):
    grouped_records = []
    acc_list = []
    for r in records:
        if r == '':
            grouped_records.append(acc_list)
            acc_list = []
        else:
            acc_list.append(r)
    if len(acc_list) > 0:
        grouped_records.append(acc_list)
    if verbose:
        print("grouped_records = %s" % grouped_records)
    return grouped_records


def manage_yes_answer(records, verbose=False):
    grouped_records = group_records(records, verbose)
    grouped_sort_records = []
    for g in grouped_records:
        s = set()
        for r in g:
            for c in r:
                s.add(c)
        grouped_sort_records.append(s)
    if verbose:
        print("grouped_sort_records = %s" % grouped_sort_records)
        print(map(len, grouped_sort_records))
    result = sum(map(len, grouped_sort_records))
    if verbose:
        print("result = %s " % result)
    return result


def manage_all_same_result(records, verbose=True):
    grouped_records = group_records(records, verbose)
    grouped_sort_records = []
    for g in grouped_records:
        s = list(set.intersection(*map(set, g)))
        grouped_sort_records.append(s)
    if verbose:
        print("grouped_sort_records = %s" % grouped_sort_records)
        print(map(len, grouped_sort_records))
    result = sum(map(len, grouped_sort_records))
    if verbose:
        print("result = %s " % result)
    return result


print(manage_yes_answer(samples, verbose=True))
print(manage_all_same_result(samples, verbose=True))

print("--- PART 1 ---")

print(manage_yes_answer(records))

print("--- PART 2 ---")
print(manage_all_same_result(records))
