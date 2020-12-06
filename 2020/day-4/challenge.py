#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import itertools
import functools
import operator
import re

records = [l.rstrip('\n') for l in sys.stdin]

grouped_records = []
current_records = []
for r in records:
    if r == '':
        grouped_records.append(current_records)
        current_records = []
    else:
        current_records.append(r)

mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
optional_field = ['cid']
rec = [
    functools.reduce(operator.iconcat, [[s for s in r.split(' ')]
                                        for r in rec], [])
    for rec in grouped_records
]

pattern = re.compile(r'(?P<key>[^:]*):(?P<value>[^:]*)')

fields_rec = [[pattern.match(s).group('key') for s in r] for r in rec]

print("--- PART 1 ---")

valid = [all(m in r for m in mandatory_fields) for r in fields_rec]

print(sum([1 for v in valid if v]))

print("--- PART 2 ---")

first_filter = [i for i in itertools.compress(rec, valid)]

passport_rec = [[(pattern.match(s).group('key'),
                  pattern.match(s).group('value')) for s in r]
                for r in first_filter]
fields = mandatory_fields + optional_field
passport_rec = [
    sorted(r, key=lambda x: fields.index(x[0])) for r in passport_rec
]
print(passport_rec)


def valid_height(hgt):
    v = int(hgt[:len(hgt) - 2])
    if 'cm' in hgt:
        return 150 <= v < 193
    else:
        return 59 <= v < 76


validation_field = {
    'byr':
    lambda x: re.match(r'[0-9]{4}', x) and 1920 <= int(x) <= 2002,
    'iyr':
    lambda x: re.match(r'[0-9]{4}', x) and 2010 <= int(x) <= 2020,
    'eyr':
    lambda x: re.match(r'[0-9]{4}', x) and 2020 <= int(x) <= 2030,
    'hgt':
    lambda x: re.match(r'[0-9]*cm|[0-9]*in', x) is not None and valid_height(x
                                                                             ),
    'hcl':
    lambda x: re.match(r'#[0-9a-f]{6}', x) is not None,
    'ecl':
    lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid':
    lambda x: re.match(r'[0-9]{9}', x) is not None,
    'cid':
    lambda x: True
}
print([[(f[0], validation_field[f[0]](f[1]), f[1]) for f in r]
       for r in passport_rec])
t = [
    functools.reduce(operator.and_, [validation_field[f[0]](f[1])
                                     for f in r], True) for r in passport_rec
]
print('\n'.join(map(str, [z for z in zip(t, passport_rec) if z[0]])))
print(sum([1 for z in t if z]))
