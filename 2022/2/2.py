#! /usr/bin/env python

test_input = open("sample.txt").read()
input = open("input.txt").read()


def partA(input):
  total_score = 0
  for line in input.rstrip().split("\n"):
    score = 0
    opponent, you = line.split(" ")
    match you:
      case "X":
        score += 1
        if opponent == "A":
          score += 3
        if opponent == "C":
          score += 6
      case "Y":
        score += 2
        if opponent == "B":
          score += 3
        if opponent == "A":
          score += 6
      case "Z":
        score += 3
        if opponent == "C":
          score += 3
        if opponent == "B":
          score += 6
    total_score += score
  return total_score


print("test partA:", partA(test_input))
print("partA:", partA(input))


def partB(input):
  total_score = 0
  for line in input.rstrip().split("\n"):
    score = 0
    opponent, result = line.split(" ")
    match result:
      case "X":
        if opponent == "A":
          score += 3
        if opponent == "B":
          score += 1
        if opponent == "C":
          score += 2
      case "Y":
        score += 3
        if opponent == "A":
          score += 1
        if opponent == "B":
          score += 2
        if opponent == "C":
          score += 3
      case "Z":
        score += 6
        if opponent == "A":
          score += 2
        if opponent == "B":
          score += 3
        if opponent == "C":
          score += 1
    total_score += score
  return total_score


print("test partB:", partB(test_input))
print("partB:", partB(input))
