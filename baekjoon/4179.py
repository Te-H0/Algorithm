from fileinput import nextfile
import sys
from collections import deque
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

r, c = map(int, sys.stdin.readline().split())
maze = [(list(sys.stdin.readline().rstrip())) for _ in range(r)]
s_i = 0  # jihoon start i
s_j = 0  # jihoon start j
fire_idx = []
for i in range(r):
    for j in range(c):
        if maze[i][j] == 'J':
            s_i = i
            s_j = j
        elif maze[i][j] == 'F':
            maze[i][j] = 1
            fire_idx.append((i, j))
        elif maze[i][j] == '.':
            maze[i][j] = 0


def fire():
    dq = deque()
    for i, j in fire_idx:
        dq.append((i, j, 1))
        maze[i][j] = 1
    while dq:
        i, j, time = dq.popleft()

        for m_i, m_j in move:
            n_i, n_j = i+m_i, j+m_j

            if n_i in range(r) and n_j in range(c) and maze[n_i][n_j] == 0:
                maze[n_i][n_j] = time + 1
                dq.append((n_i, n_j, time+1))


def bfs():
    dq = deque()
    dq.append((s_i, s_j, 1))
    maze[s_i][s_j] = -1
    while dq:
        i, j, time = dq.popleft()
        for m_i, m_j in move:
            n_i, n_j = i+m_i, j+m_j
            if n_i in range(r) and n_j in range(c):
                if maze[n_i][n_j] != -1 and maze[n_i][n_j] != '#' and (maze[n_i][n_j] == 0 or maze[n_i][n_j] > time + 1):
                    dq.append((n_i, n_j, time + 1))
                    maze[n_i][n_j] = -1
            else:
                return time
    return -1


fire()
result = bfs()
if result == -1:
    print("IMPOSSIBLE")
else:
    print(result)
