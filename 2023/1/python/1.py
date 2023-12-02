#!/usr/bin/env python

from simpleparse.parser import Parser
import time

test_input = open("../sample.txt").read()
final_input = open("../input.txt").read()

grammar = """
integer := [0-9]
<alpha> := -integer+
all     := (integer/alpha)+
"""
parser = Parser(grammar, 'all')

# 33874865052 - too high
# 33874864910 - high


def partA(input):
  tic = time.perf_counter()
  total = 0
  for line in input.splitlines():
    digits = [char for char in line if char.isnumeric()]
    total += int(digits[0] + digits[-1])
  toc = time.perf_counter()
  print(f"partA completed in in {toc - tic:0.4f} seconds")
  return total


def partB(input):
  total = 0
  spelled_ints = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
  for line in input.splitlines():
    digits = []
    for i, c in enumerate(line):
      if c.isnumeric(): digits.append(c)
      for word, digit in spelled_ints.items():
        if line[i:].startswith(word):
          digits.append(str(digit))
    total += int(digits[0] + digits[-1])
  return total


def parseA(input):
  tic = time.perf_counter()
  total = 0
  for line in input.split("\n"):
    if line != "":
      parser.parse(line)
      integers = ([int(line[x[1]:x[2]]) for x in parser.parse(line)[1]])
      total += int(str(integers[0]) + str(integers[-1]))
  toc = time.perf_counter()
  print(f"parseA completed in in {toc - tic:0.4f} seconds")
  return total



# print("test partA:", partA(open("sample.txt").read()))
print("partA:", partA(open("../input.txt").read()))
print("parseA:", parseA(open("../input.txt").read()))
# print("test partB:", partB(open("sample_2.txt").read()))
# print("partB:", partB(open("input.txt").read()))
