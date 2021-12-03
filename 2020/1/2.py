#!/usr/bin/env python

import sys

numbers = []

f = open("input.txt", 'r')
for x in f:
  numbers.append(int(x.rstrip()))

for i in numbers:
  numbers_j = numbers.copy()  # Like before, maybe overkill.
  numbers_j.remove(i)
  for j in numbers_j:
    numbers_k = numbers_j.copy()  # Almost definitely overkill.
    numbers_k.remove(j)
    for k in numbers_k:
      if (i + j + k) == 2020:
        print("{} + {} + {} = 2020".format(i, j, k))
        print("Multiplication: {}".format(i * j * k))
        sys.exit(0)
