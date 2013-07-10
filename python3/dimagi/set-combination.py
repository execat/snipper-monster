#!/usr/bin/env python
import itertools

def combination(xss):
  number_of_lists = len(xss)
  for f in xss:
    f.sort()
  ans = list(itertools.product(*xss))
  status = []

  for tup in ans:
    if sorted(tup) == list(tup):
      status.append(1)
    else:
      status.append(0)

  # print(ans)
  # print(status)
  # print(list(itertools.compress(ans, status)))

  # d for d, s in zip(data, selectors) if s
  return list(itertools.compress(ans, status))

xss = [
  ["apple", "banana", "pear"],
  ["car", "truck"],
  ["zambia", "malawi", "kenya"]
]

print(combination(xss))