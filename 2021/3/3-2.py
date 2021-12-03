#!/usr/bin/env python
from collections import Counter

result = list((l.strip()) for l in open("input.txt").readlines())


def reduce(result, bit_loc, criteria="most"):
  bits = []
  for i in range(0, len(result[0])):
    bits.append("")
    for j in range(0, len(result)):
      bits[i] += result[j][bit_loc]
  
  for b in bits:
    b = Counter(b)
    if criteria == "most":
      common_value = b.most_common()[0][0]
    else:
      common_value = b.most_common()[1][0]
    most_common_amount = b.most_common()[0][1]
    least_common_amount = b.most_common()[1][1]
    if most_common_amount == least_common_amount:
      if criteria == "most":
        common_value = 1
      else:
        common_value = 0

    inp = [i for i in result if i[bit_loc] == str(common_value)]
    if len(inp) == 1:
      # There is only one number left in our input list so we can return it
      return inp[0]
    return reduce(inp, bit_loc + 1, criteria=criteria)


print(int(reduce(result, 0, criteria="most"), 2) * int(reduce(result, 0, criteria="least"), 2))
# # 2775870 - correct
#!/usr/bin/env python
from collections import Counter

result = list((l.strip()) for l in open("input.txt").readlines())


def reduce(result, bit_loc, criteria="most"):
  bits = []
  for i in range(0, len(result[0])):
    bits.append("")
    for j in range(0, len(result)):
      bits[i] += result[j][bit_loc]
  
  for b in bits:
    b = Counter(b)
    if criteria == "most":
      common_value = b.most_common()[0][0]
    else:
      common_value = b.most_common()[1][0]
    most_common_amount = b.most_common()[0][1]
    least_common_amount = b.most_common()[1][1]
    if most_common_amount == least_common_amount:
      if criteria == "most":
        common_value = 1
      else:
        common_value = 0

    inp = [i for i in result if i[bit_loc] == str(common_value)]
    if len(inp) == 1:
      # There is only one number left in our input list so we can return it
      return inp[0]
    return reduce(inp, bit_loc + 1, criteria=criteria)


print(int(reduce(result, 0, criteria="most"), 2) * int(reduce(result, 0, criteria="least"), 2))
# # 2775870 - correct
