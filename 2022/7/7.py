#! /usr/bin/env python

test_input = open("sample.txt").read()
input = open("input.txt").read()


def partA(input):
  sumtotal = 0
  commands = []
  directories = {}
  cwd = ""
  input = input.rstrip().replace("$ cd", "$ cd %").replace("$ ls\n", "")
  print(input)
  for dir in input.split("$ cd "):
    commands.append(dir)
  commands.pop(0)
  print(commands)

  for d in commands:
    e = d.rstrip("\n").split("\n")
    print(e)
    directory = e.pop(0).replace("% ", "")
    dirsize = 0
    if directory == "..":
      cwd = "/".join(cwd.split("/")[:-1])
    elif directory == "/":
      pass
    else:
      cwd = cwd + "/" + directory
    for f in e:
      if f.startswith("dir "):
        continue
      filesize, _ = f.split()
      dirsize += int(filesize)
    print("cwd {} size {}".format(cwd,dirsize))
    if cwd in directories:
      directories[cwd] += dirsize
    else:
      directories[cwd] = dirsize
  print(directories)
  for x in directories:
    if directories[x] <= 100000:
      sumtotal += directories[x]
  #     print(int(filesize))
    # for f in e:
    #   print(f)

def partB(input):
  pass


print("test partA:", partA(test_input))
# print("partA:", partA(input))

# print("test partB:", partB(test_input))
# print("partB:", partB(input))
