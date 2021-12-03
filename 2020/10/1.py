#!/usr/bin/env python

import sys

with open('input.txt') as f:
  lines = sorted([int(x) for x in f.readlines()])

# jolt = 0
# i = 0
# differences = {1:1, 2:0, 3:1}

# line_pos = 0
# print(len(lines))
# while line_pos < len(lines):
#   success = False
#   print("LINE_POS", line_pos)
#   line_val = lines[line_pos]
#   valid_options = []
#   for x in range(line_val+1, line_val+4): valid_options.append(x)
#   window = []
#   for i, num in enumerate(lines):
#     if num in valid_options:
#       success = True
#       line_pos = i
#       print("Setting line_pos to {}".format(line_pos))
#       differences[num - line_val] += 1
#       break
#   if success is False:
#     break
# print(differences)
# print(differences[1] * differences[3])


diffs_dict = {1:1, 2:0, 3:1}

for i, num in enumerate(lines[:-1]):
  diffs_dict[lines[i+1] - num] += 1

print(diffs_dict[1] * diffs_dict[3])


