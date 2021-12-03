#!/usr/bin/env python

# Nicer file loading from https://github.com/spod/aoc/blob/main/2021/day01.py
directions = list((l.strip()) for l in open("input.txt").readlines())

horiz, depth, aim = 0, 0, 0

for x in directions:
  direction, y = x.split()
  length = int(y)
  match direction:
    case 'forward':
      horiz += length
      depth += abs(aim) * length
    case 'up': aim -= length
    case 'down': aim += length

print(abs(horiz) * abs(depth))
# 1251263225 - correct
