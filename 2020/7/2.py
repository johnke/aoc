#!/usr/bin/env python

import sys
import re

parent_bags = {}
total = 0


def find_bag_children(parents, cb, n=1):
  global total
  if parents[cb]:
    for bag in parents[cb]:
      v = int(parents[cb][bag])
      total += (v * n)
      find_bag_children(parents, bag, n * v)


f = open("input.txt", 'r')
lines = f.read().splitlines()
for l in lines:
  parent_bag, child_bags = l.split("bags contain")
  parent_bag = parent_bag.strip()
  parent_bags[parent_bag] = {}
  for cb in child_bags.split(","):
    cb = cb.lstrip()
    if cb == "no other bags.":
      pass
    else:
      cbs = re.sub(r'bag(s)?(.)?', "", cb).rstrip().split(" ")
      child_bag_amount = cbs[0]
      child_bag = " ".join(cbs[1:])
      parent_bags[parent_bag][child_bag] = child_bag_amount

find_bag_children(parent_bags, "shiny gold")
print("Total number of bags needed: {}".format(total))
