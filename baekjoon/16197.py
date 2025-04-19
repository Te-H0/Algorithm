import sys
from collections import deque

move = [(0, -1), (0, 1), (1, 0), (-1, 0)]


def bfs(position):
    dq = deque()
    dq.append((position, 0))

    while dq:
        pos, cnt = dq.popleft()
        # print(pos, cnt)
        if cnt > 10:
            continue
        if (-1, -1) in pos:
            return cnt
        

        for m_x, m_y in move:
            n_a = (pos[0][0] + m_x, pos[0][1] + m_y)
            n_b = (pos[1][0] + m_x, pos[1][1] + m_y)
            n_pos = []

            if not (0 <= n_a[0] < n) or not (0 <= n_a[1] < m):
                n_a = (-1, -1)
            elif graph[n_a[0]][n_a[1]] == "#":
                n_a = pos[0]

            if not (0 <= n_b[0] < n) or not (0 <= n_b[1] < m):
                n_b = (-1, -1)
            elif graph[n_b[0]][n_b[1]] == "#":
                n_b = pos[1]

            if n_a[0] + n_b[0] != -2:
                n_pos = [n_a, n_b]
                n_pos.sort()
                
                if n_pos[0] + n_pos[1] not in check:
                    dq.append((n_pos, cnt + 1))
                    check.add(n_pos[0] + n_pos[1])
    return -1


n, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    li = list(sys.stdin.readline().rstrip())
    graph.append(li)

check = set()
tmp = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == "o":
            tmp.append((i, j))
            if len(tmp) == 2:
                break

tmp.sort()
check.add(tmp[0] + tmp[1])
print(bfs(tmp))


# [((i,j), (k,l))]
