#! /usr/bin/env python

test_input = open("sample.txt").read()
input = open("input.txt").read()


def partA(input):
  matches = 0
  for line in input.rstrip().split("\n"):
    a, b = line.split(",")
    x = set(range(int(a.split("-")[0]), int(a.split("-")[1]) + 1))
    y = set(range(int(b.split("-")[0]), int(b.split("-")[1]) + 1))
    if x.issubset(y) or y.issubset(x):
      matches += 1
  return matches


print("test partA:", partA(test_input))
print("partA:", partA(input))


def partB(input):
  matches = 0
  for line in input.rstrip().split("\n"):
    a, b = line.split(",")
    x = set(range(int(a.split("-")[0]), int(a.split("-")[1]) + 1))
    y = set(range(int(b.split("-")[0]), int(b.split("-")[1]) + 1))
    if list(set(x).intersection(y)) != []:
      matches += 1
  return matches


print("test partB:", partB(test_input))
print("partB:", partB(input))
