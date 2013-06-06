"""
in1 = "{{[{{{{}}{{}}}[]}[][{}][({[(({{[][()()]}}{[{{{}}}]}))][()]{[[{((()))({}(())[][])}][]()]}{()[()]}]})][]]}{{}[]}}"
#in1 = input()
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
"""

#!/usr/bin/env python
import sys

def main(args):
    try:
        with open(args[1]) as f:
            stream = f.read()
    except IndexError:
        print "usage: pal.py file"
        return 0
    except IOError:
        print "error: could not open file '%s'." % args[1]
        return 1

    longest = ""

    for i, _ in enumerate(stream):
        for j, _ in enumerate(stream[i:]):
            if stream[i:j] == stream[j-1:i-1:-1] and j - i > len(longest):
                longest = stream[i:j]

    print longest

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
