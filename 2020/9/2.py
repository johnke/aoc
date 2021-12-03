#!/usr/bin/env python

import sys
import numpy as np

with open('input.txt') as f:
  lines = [int(x) for x in f.read().splitlines()]

x = 0
y = 0
target = 105950735

# while sum(lines[x:y]) != target:
#   y += 1
#   if sum(lines[x:y]) > target:
#     x += 1
#     y = x
# max_n = max(lines[x:y])
# min_n = min(lines[x:y])
# print("max: {}, min: {}, sum: {}".format(max_n, min_n, (max_n + min_n)))


print(np.convolve(lines, np.ones(25, dtype=int), 'valid'))
