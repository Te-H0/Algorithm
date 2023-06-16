import sys
from collections import deque
n, m = map(int, input().split())

l = list()
dq = deque()

for i in range(n):
    l.append(list(map(int, input())))


def bfs():
    move_x = [1, 0, -1, 0]
    move_y = [0, 1, 0, -1]
    result = True
    dq.append([0, 0, 0])
    while dq:
        now = dq.popleft()

        if now[0] == n-1 and now[1] == m-1:
            return now[2]

        for i in range(4):
            if now[0]+move_y[i] >= 0 and now[0]+move_y[i] < n and now[1]+move_x[i] >= 0 and now[1]+move_x[i] < m and l[now[0]+move_y[i]][now[1]+move_x[i]] == 1:
                l[now[0]+move_y[i]][ now[1]+move_x[i]] = 0
                dq.append([now[0]+move_y[i], now[1]+move_x[i], now[2]+1])


print(bfs()+1)
