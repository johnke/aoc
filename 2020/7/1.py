#!/usr/bin/env python

import sys
import re

parent_bags = {}
total_bags = []

def find_bag_parents(parents, cb):
  results = []
  for k, v in parents.items():
    if cb in v:
      results.append(k)
      if k not in total_bags:
        total_bags.append(k)
  for c in results:
    find_bag_parents(parents, c)


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

find_bag_parents(parent_bags, "shiny gold")
print("Total number of bags: {}".format(len(total_bags)))
