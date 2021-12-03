#!/usr/bin/env python

prev = 100000
num_increases = 0

f = open("input.txt", 'r')
for x in f:
  y = int(x.rstrip())
  if y > prev:
    num_increases += 1
  prev = y

print(num_increases)
# 1482 - correct
