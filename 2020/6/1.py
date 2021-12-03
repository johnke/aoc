#!/usr/bin/env python

import sys

a = 0

f = open("input.txt", 'r')
lines = [i.replace("\n", "") for i in f.read().split("\n\n")]
for line in lines:
  a += len(''.join(set(line)))
print("Sum of questions answered: {}".format(a))
