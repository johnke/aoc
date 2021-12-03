#!/usr/bin/env python

import sys
col = 0
trees = 0

f = open("example.txt", 'r')
lines = f.read().splitlines()

for x in lines:
  if col >= len(x) - 1:
    col = col - len(x)
  if x.rstrip()[col] == "#":
    trees += 1
  col += 3

print("Trees encountered: {}".format(trees))
