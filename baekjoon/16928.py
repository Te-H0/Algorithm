import sys
from collections import defaultdict, deque

# 사다리, 뱀
n, m = map(int, sys.stdin.readline().split())
dash = []  # 사다리, 뱀이 시작되는 위치
visit = [False] * 101
di = defaultdict()  # 사다리, 뱀 탑승했을 때 도착 위치

for _ in range(n + m):
    x, y = map(int, sys.stdin.readline().split())
    dash.append(x)
    di[x] = y

dq = deque()
dq.append((1, 0))  # 위치, 횟수
visit[1] = True
answer = []
while dq:
    idx, cnt = dq.popleft()

    if idx == 100:
        print(cnt)
        break

    else:
        for i in range(6, 0, -1):
            if idx + i <= 100 and not visit[idx + i]:
                visit[idx + i] = True
                if idx + i in dash:
                    dq.append((di[idx + i], cnt + 1))
                    visit[di[idx + i]] = True
                else:
                    dq.append((idx + i, cnt + 1))

# 2 1
# 2 60
# 30 98
# 65 25

# 사다리
# 2 60
# 30 98

# 뱀
# 65 25

# 1 -> 2 => 60 -> 65 => 25 -> 30 => 98 -> 100
