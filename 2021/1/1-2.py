#!/usr/bin/env python

depths = []
prev = 100000
num_increases = 0

f = open("input.txt", 'r')
for x in f:
  depths.append(int(x.rstrip()))

for i in range(0, len(depths)):
  total = sum(depths[i:i + 3])
  if total > prev:
    num_increases += 1
  prev = total

print(num_increases)
# 1518 - correct
