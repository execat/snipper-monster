#!/usr/bin/env python
"""
From: original content
Checks for a position where the string is not balanced (96 in this case)

Was a part of some online coding contest, that I don't recollect.

"""

in1 = "{{[{{{{}}{{}}}[]}[][{}][({[(({{[][()()]}}{[{{{}}}]}))][()]{[[{((()))({}(())[][])}][]()]}{()[()]}]})][]]}{{}[]}}"
# in1 = input()
stack = []

for (i, a) in enumerate(in1 ):
    if (a is '{') | (a is '[') | (a is '('):
        stack.append(a)
    if (a == '}') | (a == ']') | (a == ')'):
        tmp = stack.pop()
        if (((a == ']') & (tmp == '[')) | ((a == '}') & (tmp == '{')) | ((a == ')') & (tmp == '('))):
            continue;
        else:
            print(i)
            break