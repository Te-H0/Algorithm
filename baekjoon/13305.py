import sys


n = int(sys.stdin.readline())
dist = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))
cost.insert(0, int(1e9))

min_idx = 0
cost_idx = 1
ans = 0

for d in dist:
    if cost[cost_idx] < cost[min_idx]:
        min_idx = cost_idx
    ans += d * cost[min_idx]
    cost_idx += 1

print(ans)
