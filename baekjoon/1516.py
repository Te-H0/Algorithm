import sys
from collections import deque

n = int(sys.stdin.readline())
li = []
build_time = [0] * n
required_li = [[] for _ in range(n)]
required_cnt = [0] * n
answer = [0] * n
for i in range(n):
    tmp_li = list(map(int, sys.stdin.readline().split()))

    build_time[i] += tmp_li[0]
    tmp_li = tmp_li[1:-1]
    li.append(tmp_li)
    for l in tmp_li:
        required_li[l - 1].append(i)
        required_cnt[i] += 1

dq = deque()

for i in range(n):
    if required_cnt[i] == 0:
        dq.append(i)
        answer[i] = build_time[i]
while dq:
    x = dq.popleft()

    for r in required_li[x]:
        required_cnt[r] -= 1
        if required_cnt[r] == 0:
            dq.append(r)
            tmp = []
            for l in li[r]:

                tmp.append(answer[l - 1])
            answer[r] = max(tmp) + build_time[r]
            # answer[r] = answer[x] + build_time[r]

for a in answer:
    print(a)
