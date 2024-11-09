import sys
from collections import deque

move = [(-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)]


def bfs(l, start, end):
    visit = [[False] * l for _ in range(l)]
    dq = deque()
    dq.append((start[0], start[1], 0))
    visit[start[0]][start[1]] = True

    while dq:
        x, y, c = dq.popleft()
        if x == end[0] and y == end[1]:
            return c
        for m_x, m_y in move:
            n_x = x + m_x
            n_y = y + m_y
            if n_x in range(0, l) and n_y in range(0, l) and not visit[n_x][n_y]:
                dq.append((n_x, n_y, c + 1))
                visit[n_x][n_y] = True
                
t = int(sys.stdin.readline())

for _ in range(t):
    l = int(sys.stdin.readline())
    s_x, s_y = map(int, sys.stdin.readline().split())
    e_x, e_y = map(int, sys.stdin.readline().split())
    print(bfs(l,(s_x,s_y),(e_x,e_y)))