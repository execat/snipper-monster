#!/usr/bin/env python

def without_7(lim):
  list = []
  for num in range(1, lim+1):
    string = str(num)
    if (string.find("7") == -1):
      list.append(num)

  return len(list)

print(without_7(100))
