#! /usr/bin/env python

test_input = open("sample.txt").read()
input = open("input.txt").read()


def get_char_values(items):
  total = 0
  for item in items:
    item_value = ord(item) - 96
    if item_value < 0:
      item_value += 58
    total += item_value
  return total


def partA(input):
  total_items = []
  for line in input.rstrip().split("\n"):
    comp1 = list(line[:len(line) // 2])
    comp2 = list(line[len(line) // 2:])
    common = list(set(comp1).intersection(comp2))
    total_items += common
  return get_char_values(total_items)


print("test partA:", partA(test_input))
print("partA:", partA(input))


def partB(input):
  total_items = []
  foo = list(map(lambda s: s.rstrip('\n'), input.rstrip("\n").split("\n")))
  for group_number in range(0, len(foo), 6):
    rucksacks = foo[group_number:group_number + 6]
    comp1_a, comp1_b, comp1_c = iter(rucksacks[:len(rucksacks) // 2])
    total_items += list(set(comp1_a).intersection(comp1_a, comp1_b, comp1_c))
    comp2_a, comp2_b, comp2_c = iter(rucksacks[len(rucksacks) // 2:])
    total_items += list(set(comp2_a).intersection(comp2_a, comp2_b, comp2_c))
  return get_char_values(total_items)


print("test partB:", partB(test_input))
print("partB:", partB(input))
