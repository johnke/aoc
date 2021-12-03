#!/usr/bin/env python

from icecream import ic
import math

result = list((l.strip()) for l in open("input.txt").readlines())

total = 0
for present in result:
  x = [int(n) for n in present.split("x")]
  total += (2 * (sorted(x)[0] + sorted(x)[1])) + math.prod(x)

print(total)
