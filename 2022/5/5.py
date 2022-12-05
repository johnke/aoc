#! /usr/bin/env python

import re

test_input = open("sample.txt").read()
input = open("input.txt").read()


def partA(input):
  num_cols = int((len(input.split("\n")[0]) + 1) / 4)
  stacks = []
  [stacks.append([]) for i in range(0, num_cols)]

  for line in input.rstrip().split("\n"):
    if re.match(r".*\[\S\].*", line):
      for i in range(0, num_cols):
        crate = line[(4 * i) + 1]
        if crate != " ":
          stacks[i].append(crate)
    m = re.match(r"move (\d+) from (\d+) to (\d+)", line)
    if m:
      amount = int(m.group(1))
      col_from = int(m.group(2)) - 1
      col_to = int(m.group(3)) - 1
      for j in range(0, amount):
        moved = stacks[col_from].pop(0)
        stacks[col_to].insert(0, moved)
  return "".join([s[0] for s in stacks])


print("test partA:", partA(test_input))
print("partA:", partA(input))


def partB(input):
  num_cols = int((len(input.split("\n")[0]) + 1) / 4)
  stacks = []
  [stacks.append([]) for i in range(0, num_cols)]

  for line in input.rstrip().split("\n"):
    if re.match(r".*\[\S\].*", line):
      for i in range(0, num_cols):
        crate = line[(4 * i) + 1]
        if crate != " ":
          stacks[i].append(crate)
    m = re.match(r"move (\d+) from (\d+) to (\d+)", line)
    if m:
      amount = int(m.group(1))
      col_from = int(m.group(2)) - 1
      col_to = int(m.group(3)) - 1
      moved = stacks[col_from][:amount]
      stacks[col_from] = stacks[col_from][amount:]
      stacks[col_to] = moved + stacks[col_to]
  return "".join([s[0] for s in stacks])


print("test partB:", partB(test_input))
print("partB:", partB(input))
