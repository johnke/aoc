#!/usr/bin/env python

from functools import reduce


def partA(input):
  limits = {
    "red": 12,
    "green": 13,
    "blue": 14
  }
  games_sum = 0
  for line in input.splitlines():
    games_to_add = True
    game_id, games = line.split(":")
    game_id = int(game_id.replace("Game ", ""))
    for draw in games.split(";"):
      for colors in draw.split(","):
        amount, color = colors.lstrip().split(" ")
        if int(amount) > limits[color]:
          games_to_add = False
    if games_to_add is True:
      games_sum += game_id
  return games_sum


def partB(input):
  games_sum = 0
  for line in input.splitlines():
    max_colors = {
      "red": 0,
      "green": 0,
      "blue": 0,
    }
    game_id, games = line.split(":")
    game_id = int(game_id.replace("Game ", ""))
    for draw in games.split(";"):
      for colors in draw.split(","):
        amount, color = colors.lstrip().split(" ")
        if int(amount) > max_colors[color]:
          max_colors[color] = int(amount)
    games_sum += reduce(lambda x, y: x * y, max_colors.values())
  return games_sum


print("test partA:", partA(open("../sample.txt").read()))
print("partA:", partA(open("../input.txt").read()))
print("test partB:", partB(open("../sample.txt").read()))
print("partB:", partB(open("../input.txt").read()))
