#!/usr/bin/env python

import sys

valid_password = 0

f = open("input.txt", 'r')
for x in f:
  n, l, p = x.rstrip().split(' ')
  num_l, num_h = [int(i) for i in n.split("-")]
  l = l.strip(":")
  occur = p.count(l)
  if occur >= int(num_l) and occur <= num_h:
    valid_password += 1

print("Total valid passwords: {}".format(valid_password))
