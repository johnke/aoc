#!/usr/bin/env python

import sys
import numpy

f = open("input.txt", 'r')
lines = f.read().splitlines()

seat_ids = []


def get_number(bsp_str, amount):
  row_nums = list(range(amount))
  for i in bsp_str:
    if i in ["F", "L"]:
      row_nums = row_nums[:-int((len(row_nums)/2)) or None]
    elif i in ["B", "R"]:
      row_nums = row_nums[-int((len(row_nums)/2)):]
  return row_nums


for line in lines:
  row_str = line[:-3]
  seat_str = line[-3:]
  row_num = get_number(row_str, 127)[0]
  seat_num = get_number(seat_str, 8)[0]
  seat_ids.append((row_num * 8) + seat_num)

print("Highest seat ID is: {}".format(max(seat_ids)))
compare = list(range(min(seat_ids), max(seat_ids)+1))
print(set(compare) - set(sorted(seat_ids)))
