#!/usr/bin/env python

import sys

with open('input.txt') as f:
  lines = sorted([int(x) for x in f.readlines()])

arrange_dict = {d: 1 for d in [0] + lines}
for l in lines:
  arrange_dict[l] = sum(arrange_dict[l - i] for i in [1, 2, 3] if l - i in arrange_dict)

print(arrange_dict[lines[-1]])


