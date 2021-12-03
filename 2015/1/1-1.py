#!/usr/bin/env python

from collections import Counter
from icecream import ic

result = list((l.strip()) for l in open("input.txt").readlines())

print(result)

for floor in result:
  floor = Counter(floor)
  print(floor['('] - floor[')'])
