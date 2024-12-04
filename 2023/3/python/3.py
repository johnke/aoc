#!/usr/bin/env python

from simpleparse.parser import Parser
from simpleparse.common import numbers, strings
import re
from pprint import pprint

grammar = """
integer := [0-9]+
<alpha> := -integer+
<dot> := "."+
<symbol> := '*' / '#' / '-' / '+' / '@' / '%' / '&' / '=' / '$' / '/'
all     := (integer/dot/symbol/alpha)+
"""

parser = Parser(grammar, 'all')
# symbol_parser = Parser(grammar, 'symbol')
# dot_parser = Parser(grammar, 'dot')
# integer_parser = Parser(grammar, 'integer')
# test_line = ".....+.58."
# integer_parser.parse(test_line)


def partA(input):
  total = 0
  input_list = list(input.splitlines())
  for i, line in enumerate(input_list):
    success, tree, _ = parser.parse(line)
    if tree:
      for integers in tree:
        surrounding_string = ""
        part_numbers = line[integers[1]:integers[2]]
        for offset in [-1, 0, 1]:
          line_number = max(i + offset, 0)
          line_number = min(line_number, len(input_list)-1)
          pos_start = max(integers[1] - 1, 0)
          pos_end = min(integers[2] + 1, len(line))
          line_slice = input_list[line_number][pos_start:pos_end]
          surrounding_string += line_slice
        surrounding_string = re.sub("\d", "", surrounding_string).replace(".", "")
        if surrounding_string != "":
          total += int(part_numbers)
  return total


def find_numbers_on_line(line):
  s, t, _ = parser.parse(line)
  if t:
    return t


# 85195075 - too low
# 117485874 - too high
# 100723006 - too high

full_pattern = re.compile('[^0-9]')

def partB(input):
  total = 0
  input_list = list(input.splitlines())
  for i, line in enumerate(input_list):
    for star_i, l in enumerate(line):
      if l == "*":
        print("Found * on", i+1, star_i)
        matched_numbers = []
        for offset in [-1, 0, 1]:
          found_numbers = []
          search_line_number = max(i + offset, 0)
          search_line_number = min(i + offset, len(input_list))
          print("Searching line", search_line_number + 1)
          # * is found at star_i,
          # so we need to search previous line for star_i - 1, star_i, star_i +1
          # also need to search next line for star_i - 1, star_i, star_i + 1
          star_range = range(max(star_i - 1, 0), min(star_i + 2, len(input_list)))
          pprint(star_range)
          for index_pos in star_range:
            print("RANGE_POS", index_pos)
            search_int = input_list[search_line_number][index_pos]
            print(search_int)
            if search_int.isnumeric():
              # need to extract number from around input_list[search_line_number][index_pos]
              # and make sure we haven't seen it before
              fixed_line = re.sub(full_pattern, '.', input_list[search_line_number])
              r_sep = fixed_line.find(".", index_pos)
              if r_sep == -1:
                r_sep = len(line)
              l_sep = fixed_line.rfind(".", 0, index_pos) + 1
              num = fixed_line[l_sep:r_sep]
              b = (fixed_line, l_sep, r_sep)
              if b not in found_numbers:
                print(b, "NOT IN FOUND_NUMBERS", found_numbers)
                matched_numbers.append(num)
                found_numbers.append(b)
                print(found_numbers)
                print("Matched numbers", matched_numbers)
              # if search_line_number != i:
              #   print("BREAK -", search_line_number, i)
              #   break
        if len(matched_numbers) == 2:
          print("Multiplying", matched_numbers, "based on star on line", i+1, star_i+1)
          total += int(matched_numbers[0]) * int(matched_numbers[1])
  return total

          # s, t, _ = parser.parse(input_list[search_line_number])

# def partB(input):
#   total = 0
#   input_list = list(input.splitlines())
#   for i, line in enumerate(input_list):
#     tree = find_numbers_on_line(line)
#     if tree:
#       for integers in tree:
#         part_numbers = line[integers[1]:integers[2]]
#         # print("Found part number:", part_numbers, "on line", i)
#         for offset in [0, 1]:
#           line_number = i + offset
#           line_number = min(line_number, len(input_list)-1)
#           pos_start = max(integers[1] - 1, 0)
#           pos_end = min(integers[2] + 1, len(line))
#           line_slice = input_list[line_number][pos_start:pos_end]
#           gear_loc = input_list[line_number].find("*", pos_start, pos_end)
#           if gear_loc != -1:
#             for gear_offset in [0, 1]:
#               # print("FOUND GEAR")
#               gear_line = input_list[min(line_number + gear_offset, len(input_list) - 1)]
#               k = find_numbers_on_line(gear_line)
#               # print("checking line", line_number + gear_offset, ":", gear_line)
#               if k:
#                 for j in k:
#                   if gear_line[j[1]:j[2]] != part_numbers:
#                     x = range(j[1], j[2])
#                     y = range(pos_start - 1, pos_end + 1)
#                     xs = set(x)
#                     if xs.intersection(y):
#                       print("GEAR:", line_number, gear_loc, "Numbers:", part_numbers, gear_line[j[1]:j[2]])
#                       total += int(part_numbers) * int(gear_line[j[1]:j[2]])
#                       # print("I THINK SO?", int(gear_line[j[1]:j[2]]))
#                       break
#   return total


# def partB(input):

#   grammar_gear = """
#   <integer> := [0-9]+
#   <alpha> := -integer+
#   <dot> := "."+
#   gear := "*"
#   <symbol> := '#' / '-' / '+' / '@' / '%' / '&' / '=' / '$' / '/'
#   all     := (integer/gear/dot/symbol/alpha)+
#   """
#   grammar_integer = """
#   integer := [0-9]+
#   <alpha> := -integer+
#   <dot> := "."+
#   <symbol> := '*' / '#' / '-' / '+' / '@' / '%' / '&' / '=' / '$' / '/'
#   all     := (integer/dot/symbol/alpha)+
#   """
#   gear_parser = Parser(grammar_gear, 'all')
#   int_parser = Parser(grammar_integer, 'all')
#   total = 0
#   input_list = list(input.splitlines())
#   for i, line in enumerate(input_list):
#     print("LINE", line)
#     success, tree, _ = gear_parser.parse(line)
#     if tree:
#       for gear in tree:
#         for offset in [-1, 0, 1]:
#           print("GEAR:", gear)
#           line_number = max(i + offset, 0)
#           line_number = min(line_number, len(input_list) - 1)
#           pos_start = max(gear[1] - 1, 0)
#           pos_end = min(gear[1] + 1, len(line))
#           line_slice = input_list[line_number][pos_start:pos_end]
#           for b, c in enumerate(line_slice):
#             if c.isnumeric():
#               print("NUMBER",c)
#               for x in int_parser.parse(input_list[line_number])[1]:
#                 if gear[1] in range(min(x[1] - 1, 0), max(x[2] + 1, len(line))):
#                   print("AFJF")
#                   print("NUMBER_TO_MULTIPLY", input_list[line_number][x[1]:x[2]])
#                 print(x)
#           print(line_slice)
#   return total

# def partB(input):
#   total = 0
#   input_list = list(input.splitlines())
#   input_list = "".join(input_list)
#   input_list = re.sub("\.+", "_", input_list).split("_")
#   print(input_list)
#   for i, j in enumerate(input_list):
#     if j == "*":
#       prev_j = input_list[max(i - 1, 0)]
#       next_j = input_list[min(i + 1, len(input_list) - 1)]
#       print("previous:", prev_j, "next:", next_j)
#       if prev_j.isnumeric() and next_j.isnumeric():
#         total += int(prev_j) * int(next_j)
#   return total


# print("test partA:", partA(open("../sample.txt").read()))
# print("partA:", partA(open("../input.txt").read()))
# print("test partB:", partB(open("../sample.txt").read()))
print("partB:", partB(open("../input.txt").read()))
# symbols = []
# for line in open("../input.txt").read().splitlines():
#   line = re.sub("\d", "", line)
#   line = line.replace(".", "")
#   for symbol in line:
#     if symbol not in symbols:
#       symbols.append(symbol)
# print(symbols)
