#! /usr/bin/env python

test_input = open("sample.txt").read()
input = open("input.txt").read()


def partA(input):
  cals = list((j.strip()) for j in input.split("\n"))
  finalcals = []
  elfcals = 0
  for entry in cals:
    if entry == '':
      finalcals.append(elfcals)
      elfcals = 0
    else:
      elfcals += int(entry)
  return max(finalcals)


print("test partA:", partA(test_input))
print("partA:", partA(input))


def partB(input):
  cals = list((j.strip()) for j in input.split("\n"))
  finalcals = []
  elfcals = 0
  for entry in cals:
    if entry == '':
      finalcals.append(elfcals)
      elfcals = 0
    else:
      elfcals += int(entry)
  return sum(sorted(finalcals)[-3:])


print("test partB:", partB(test_input))
print("partB:", partB(input))
