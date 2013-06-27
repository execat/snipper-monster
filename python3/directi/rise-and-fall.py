#!/usr/bin/python3
# Question from http://www.codechef.com/problems/MARCHA4/

def solve(num, digits):
    ans = str(num ** num)
    return "%s %s" %(ans[:digits], ans[-digits:])

for i in range(int(input())):
    params = tuple(input().split())
    print(solve(int(params[0]), int(params[1])))
