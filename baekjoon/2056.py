import sys
from collections import deque

n = int(sys.stdin.readline())
time = [0] * (n + 1)
li = [[] for _ in range(n + 1)]
dp = [0] * (n + 1)
degree = [0] * (n + 1)
for i in range(1, n + 1):
    tmp = list(map(int, sys.stdin.readline().split()))
    time[i] = tmp[0]

    if tmp[1]:
        for j in range(2, len(tmp)):
            li[tmp[j]].append(i)  # 나를 선수행 노드로 갖고 있는 애들을 저장
            degree[i] += 1
            
dq = deque()

for i in range(1, n + 1):
    if degree[i] == 0:
        dq.append(i)
        dp[i] += time[i]

while dq:
    x = dq.popleft()

    for l in li[x]:
        degree[l] -= 1
        dp[l] = max(dp[x] + time[l], dp[l])
        if degree[l] == 0:
            dq.append(l)

print(max(dp))
