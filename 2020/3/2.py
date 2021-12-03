#!/usr/bin/env python

import sys
import numpy

trees = []
f = open("input.txt", 'r')
lines = f.read().splitlines()
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]


def count_trees(l, r, c):
  t = 0
  if l[r][c] == "#":
    t += 1
  return t


for slope in slopes:
  row = 0
  col = 0
  tr = 0
  col_i, row_i = slope
  while row < len(lines) - 1:
    row += row_i
    col += col_i
    if col >= len(lines[0])-1:
        col = col - len(lines[0])
    tr += count_trees(lines, row, col)
  trees.append(tr)
print("Multiplied: {}".format(numpy.prod(trees)))
