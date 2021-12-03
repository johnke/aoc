#!/usr/bin/env python

import sys
from itertools import permutations, islice

with open('input.txt') as f:
  lines = [int(x) for x in f.read().splitlines()]


def traverse_sums(preamble, target):
  hit_target = False
  preamble_unseen = preamble.copy()  # Handy local copy of our list for working
  for i in preamble:
    preamble_unseen.pop(0)
    for j in preamble_unseen:
      if (i + j) == target:
        hit_target = True
  if hit_target == True:  # this is so backwards
    return None
  return target


x = 0
line_length = len(lines)

while x <= line_length:
  hit = traverse_sums(lines[0:25], lines[25])
  if hit:
    print("Got a result:", hit)
    break
  else:
    x += 1
    lines.pop(0)
