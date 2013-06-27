#!/usr/bin/python3
# Question from http://www.codechef.com/problems/ARRAYTRM/

for f in range(int(input())):
    n, k = [int(x) for x in input().split()]
    l = [int(x) % (k + 1) for x in input().split()]
    print("YES") if max(map(l.count, set(l))) >= n-1 else print("NO")
