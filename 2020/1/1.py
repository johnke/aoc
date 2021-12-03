#!/usr/bin/env python

import sys

numbers = []

f = open("input.txt", 'r')
for x in f:
  numbers.append(int(x.rstrip()))

for num in numbers:
  local_numbers = numbers.copy()
  local_numbers.remove(num)  # This is probably overkill but better be safe!
  for i in local_numbers:
    if (num + i) == 2020:
      print("{} + {} = 2020".format(num, i))
      print("Multiplication: {}".format(num * i))
      sys.exit(0)
