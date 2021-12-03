#!/usr/bin/env python

import sys

valid = 0

f = open("input.txt", 'r')
lines = f.read().split("\n\n")

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

for line in lines:
  fields_found = []
  line = line.rstrip().replace("\n", " ").split(" ")
  for field in line:
    k, v = field.split(":")
    if k != "cid":
      fields_found.append(k)
  if sorted(fields_found) == sorted(required):
    valid += 1
print("Valid entries:", valid)
