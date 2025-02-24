from bisect import bisect_right
import sys

n, k = map(int, sys.stdin.readline().split())

rank = []
target = -1
for _ in range(n):
    x = list(map(int, sys.stdin.readline().split()))
    if x[0] == k:
        target = x[1:]
    rank.append((x[1:]))

rank.sort()
print(n - bisect_right(rank, target) + 1)
