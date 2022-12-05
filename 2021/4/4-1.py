#!/usr/bin/env python

from icecream import ic
import sys

result = list((l.strip()) for l in open("sample.txt").readlines())

result2 = "::".join(result)
boards = result2.split("::::")
numbers = (int(i) for i in boards[0].split(","))
# numbers = boards[0].split(",")
boards.pop(0)
ic(numbers)
ic(boards)

playboards = []
for idx, b in enumerate(boards):
  ic(idx)
  playboards.append([])
  c = b.split("::")
  for d in c:
    # e = d.split()
    ic(d)
    e = [int(i) for i in d.split()]
    ic(e)
    playboards[idx].append(e)
ic(playboards)

# for board in playboards:
#   workboard = board
#   row = [0, 0, 0, 0, 0]
#   col = [0, 0, 0, 0, 0]
#   print(board)

board = playboards[0]
board_results = {}
for number in numbers:
  for i, x in enumerate(board):

    col_xes = 0
    for j, a in enumerate(x):
      # ic(a)
      if number == a:
        # print("YES")
        board[i][j] = "X"
    for k in range(0, len(x)):
      if x[k] == "X":
        col_xes += 1
    if all([y == "X" for y in x]) or col_xes == 5:
      print("YES")
      print("Number: {}".format(number))
      sys.exit(0)
  print(board)
# print(board)
# called_numbers = result[0]
# result.pop(0)
# ic(result)
# ic(called_numbers)
