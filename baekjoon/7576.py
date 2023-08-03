import sys
from collections import deque
f = sys.stdin.readline
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
n, m = map(int, f().split())

l = [list(map(int, f().split()))for _ in range(m)]

start = []

for i in range(m):
    for j in range(n):
        if l[i][j] == 1:
            start.append((i, j))


def bfs():
    dq = deque()
    temp_dq = deque()
    answer = 0
    for x in start:
        dq.append((x[0], x[1], 0))

    while dq:
        while dq:
            a, b, day = dq.popleft()
            answer = day
            for i in range(4):
                if a+move[i][0] >= 0 and a+move[i][0] < m and b+move[i][1] >= 0 and b+move[i][1] < n and l[a+move[i][0]][b+move[i][1]] == 0:
                    temp_dq.append((a+move[i][0], b+move[i][1], day+1))
                    l[a+move[i][0]][b+move[i][1]] = 1

        while temp_dq:
            q, w, e = temp_dq.popleft()
            dq.append((q, w, e))

    return answer


answer = bfs()
for list in l:
    if 0 in list:
        answer = -1
        break
print(answer)
