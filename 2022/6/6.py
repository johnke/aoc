#! /usr/bin/env python

test_input = open("sample.txt").read()
input = open("input.txt").read()


def partA(input, size=4):
  line = input.rstrip().rstrip()
  for i in range(0,len(line)):
    sl = list(line[i:i+size])
    if len(list(set(sl))) == len(sl):
      return i+size

print("test partA:", partA(test_input))
print("partA:", partA(input))

print("test partB:", partA(test_input, 14))
print("partB:", partA(input, 14))
