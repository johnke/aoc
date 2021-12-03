#!/usr/bin/env python

from icecream import ic

result = list((l.strip()) for l in open("input.txt").readlines())

total = 0

for present in result:
  l, w, h = [int(n) for n in present.split("x")]
  sides = [(l * w), (w * h), (h * l)]
  paper = (sum(sides) * 2) + min(sides)
  total += paper

print(total)
# 1588178 - correct
