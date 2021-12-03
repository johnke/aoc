#!/usr/bin/env python

# Nicer file loading from https://github.com/spod/aoc/blob/main/2021/day01.py
directions = list((l.strip()) for l in open("input.txt").readlines())

horiz, depth = 0, 0

for x in directions:
  direction, y = x.split()
  length = int(y)
  match direction:
    case 'forward': horiz += length
    case 'up': depth += length
    case 'down': depth -= length

print(abs(horiz) * abs(depth))
# 1580000 - correct
