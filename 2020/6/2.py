#!/usr/bin/env python

import sys

a = 0

f = open("input.txt", 'r')
lines = [i for i in f.read().split("\n\n")]
for line in lines:
  group = line.rstrip().split("\n")
  if len(group) == 1:
    group_score = len(group[0])
    a += group_score
  else:
    letter_seen = {}
    for person in group:
      for pq in person:
        if pq in letter_seen:
          letter_seen[pq] += 1
        else:
          letter_seen[pq] = 1
    letter_remove = []
    for k, v in letter_seen.items():
      if v != len(group):
        letter_remove.append(k)
    for letter in letter_remove:
      del letter_seen[letter]
    group_score = len(letter_seen)
    a += len(letter_seen)

print("Sum of counts: {}".format(a))
