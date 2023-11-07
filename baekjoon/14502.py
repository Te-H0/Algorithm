import sys
from itertools import combinations
from copy import deepcopy
from collections import deque
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
n, m = map(int, sys.stdin.readline().split())
mapp = []
empty_area = []
answer = -1
for _ in range(n):
    mapp.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if mapp[i][j] == 0:
            empty_area.append((i, j))

combi_wal = list(combinations(empty_area, 3))


def bfs(i, j):
    check = [[False]*m for _ in range(n)]
    dq = deque()
    dq.append((i, j))
    check[i][j] = True

    while dq:
        x, y = dq.popleft()

        for m_x, m_y in move:
            n_x = x + m_x
            n_y = y + m_y

            if n_x in range(n) and n_y in range(m) and tmp_map[n_x][n_y] == 0 and not check[n_x][n_y]:
                tmp_map[n_x][n_y] = 2
                dq.append((n_x,n_y))
                check[n_x][n_y] = False

    count = 0

for w1, w2, w3 in combi_wal:
    tmp_map = deepcopy(mapp)
    tmp_map[w1[0]][w1[1]] = 1
    tmp_map[w2[0]][w2[1]] = 1
    tmp_map[w3[0]][w3[1]] = 1

    tmp = 0

    for i in range(n):
        for j in range(m):
            if tmp_map[i][j] == 2:
                bfs(i,j)
    for i in range(n):
        tmp += tmp_map[i].count(0)

    answer = max(tmp,answer)


print(answer)
