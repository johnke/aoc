#!/usr/bin/env python

import sys

f = open("input.txt", 'r')
lines = f.read().splitlines()

instructions_run = {}
accumulator = 0
pos = 0
instruction_pos = {}

for i,v in enumerate(lines):
  if v.startswith("nop") or v.startswith("jmp"):
    instruction_pos[i] = 0


def switch_value(v):
  if v == "nop":
    return "jmp"
  elif v == "jmp":
    return "nop"
  else:  # Just in case
    print("ERROR: Got neither - {}".format(v))
    sys.exit(1)


while True:
  if pos not in instructions_run.keys():
    if pos > len(lines)-1:
      break
    ins, val = lines[pos].split()
    instructions_run[pos] = ([ins, val])
    if ins == "nop":
      pos += 1
    elif ins == "acc":
      accumulator += int(val)
      pos += 1
    elif ins == "jmp":
      pos += int(val)
  else:
    i, v = list(instruction_pos.items())[0]    
    if v < 2:
      ins, val = lines[i].split()
      ins = switch_value(ins)
      instruction_pos[i] += 1
      newval = "{} {}".format(ins, val)
      lines[i] = newval
    elif v == 2:
      instruction_pos.pop(i)
    # Reset everything
    pos = 0
    instructions_run = {}
    accumulator = 0

print(accumulator)
