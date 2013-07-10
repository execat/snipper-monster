#!/usr/bin/env python
import re

def rot13(word):
  ret = []
  for i in word:
    if i.islower():
      dist = 13 if i <= 'm' else -13
    elif i.isupper():
      dist = 13 if i <= 'M' else -13
    else:
      dist = 0

    ret.append(chr(ord(i) + dist))
  return "".join(ret)

def code(inp):
  chars = re.findall('[^\w]', inp)
  words = re.split(r'[^\w]', inp)

  cipher = []
  flag = True
  for f in words:
    word = ""
    if flag:
      reverse = f[::-1]
      word = rot13(reverse)
    else:
      word = rot13(f)

    flag = not flag
    cipher.append(word)

  # print(cipher)     # Checks out
  output = []
  for index in range(len(chars)):
    output.append(cipher[index])
    output.append(chars[index])
  # print(output)     # Checks out
  return "".join(output)


def start():
  inp = input("Enter a string: ")
  # inp = "Hello world!"
  x = code(inp)
  print(code(x))

start()

