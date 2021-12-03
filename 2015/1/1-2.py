#!/usr/bin/env python

import sys

result = [(l.strip()) for l in open("input.txt").readlines()]

floor = 0
for idx, f in enumerate(result[0]):
  match f:
    case "(": floor += 1
    case ")": floor -= 1
  if floor == -1:
    print("HERE WE ARE", idx + 1)
    sys.exit(0)
