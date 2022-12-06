#! /usr/bin/env python

test_input = open("sample.txt").read()
input = open("input.txt").read()


def partA(input):
  line = input.rstrip().rstrip()
  for i in range(0,len(line)):
    sl = list(line[i:i+4])
    if len(list(set(sl))) == len(sl):
      return i+4

print("test partA:", partA(test_input))
print("partA:", partA(input))


def partB(input):
  line = input.rstrip().rstrip()
  for i in range(0,len(line)):
    sl = list(line[i:i+14])
    if len(list(set(sl))) == len(sl):
      return i+14


print("test partB:", partB(test_input))
print("partB:", partB(input))
