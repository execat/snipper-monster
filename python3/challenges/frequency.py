import collections

inp = int(input())
dic = dict()

for f in range(inp):
	dic[f] = input()

ordered = collections.Counter(dic.values()).most_common()

k_most_frequent = int(input())
pop_out = len(ordered) - k_most_frequent
print("Len", len(ordered))

for f in range(k_most_frequent):
	print(ordered[f][0])

