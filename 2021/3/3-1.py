#!/usr/bin/env python
from collections import Counter

# Nicer file loading from https://github.com/spod/aoc/blob/main/2021/day01.py
inp = list((l.strip()) for l in open("input.txt").readlines())

bits = []

gamma = ""
epsilon = ""

for i in range(0, len(inp[0])):
  bits.append("")
  for j in range(0, len(inp)):
    bits[i] += inp[j][i]

for b in bits:
  b = Counter(b)
  gamma += b.most_common()[0][0]
  epsilon += b.most_common()[1][0]

print(int(gamma, 2) * int(epsilon, 2))
# 2724524 - correct
