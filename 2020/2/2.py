#!/usr/bin/env python

import sys

valid_password = 0

f = open("input.txt", 'r')
for x in f:
  n, l, p = x.rstrip().split(' ')
  num_l, num_h = [int(i) for i in n.split("-")]
  l = l.strip(":")
  if (p[num_l-1] == l or p[num_h-1] == l) and not (p[num_l-1] == l and p[num_h-1] == l):  # I think I lost my mind here
    valid_password += 1

print("Total valid passwords: {}".format(valid_password))
