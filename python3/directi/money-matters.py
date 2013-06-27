#!/usr/bin/python3
# Question from http://www.codechef.com/problems/MONEY/
from math import sqrt

def solve(n):
    if n in dic.keys():
        return dic[n]
    if n <= 1:
        return 1
    ans = 1
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            ans += solve(n/i)
            if i != sqrt(n):
                ans += solve(i)
    dic[n] = ans
    return ans

dic = {}
for i in range(int(input())):
    print(solve(int(input()) + 1))
