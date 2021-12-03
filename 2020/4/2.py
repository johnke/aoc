#!/usr/bin/env python

import sys
import re

valid = 0

f = open("input.txt", 'r')
lines = f.read().split("\n\n")


def validate_line(line):
  """Checks each field in the line for validity.
  Returns False if any field is invalid"""
  for field in line:
    k, v = field.split(":")
    if k == "byr":
      if (int(v) < 1920) or (int(v) > 2002):
        return False
    elif k == "iyr":
      if (int(v) < 2010) or (int(v) > 2020):
        return False
    elif k == "eyr":
      if (int(v) < 2020) or (int(v) > 2030):
        return False
    elif k == "hgt":
      if v[-2:] == "cm":
        if (int(v[:-2]) < 150) or (int(v[:-2]) > 193):
          return False
      elif v[-2:] == "in":
        if (int(v[:-2]) < 59) or (int(v[:-2]) > 76):
          return False
      elif v[-2:] not in ["cm", "in"]:
        return False
    elif k == "hcl":
      if not re.search(r'^#(?:[0-9a-f]{3}){1,2}$', v):
        return False
    elif k == "ecl":
      if v not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    elif k == "pid":
      if not re.search(r'^[0-9]{9,9}$', v):
        return False
  return True


for line in lines:
  line = line.rstrip().replace("\n", " ").split(" ")
  for i in line:
    if i.startswith("cid:"):  # Remove the optional field from all lines
      line.remove(i)
  if len(line) == 7:  # Being lazy here
    if validate_line(sorted(line)) is True:
      valid += 1
print("Valid entries:", valid)
