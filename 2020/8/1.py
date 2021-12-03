#!/usr/bin/env python

import sys

f = open("input.txt", 'r')
lines = f.read().splitlines()

instructions_run = []
accumulator = 0
pos = 0

while True:
  if pos not in instructions_run:
    instructions_run.append(pos)
    ins, val = lines[pos].split()
    if ins == "nop":
      pos += 1
    elif ins == "acc":
      accumulator += int(val)
      pos += 1
    elif ins == "jmp":
      pos += int(val)
  else:
    print("Accumulator is: {}".format(accumulator))
    break
