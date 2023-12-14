import sys
from collections import deque
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m = map(int, sys.stdin.readline().split())
mapp = []
answer = -1
for _ in range(n):
    mapp.append(list(map(int, sys.stdin.readline().rstrip())))


def bfs():
    global answer
    dq = deque()
    dq.append((0, 0, 0, 1))
    checked[0][0][0] += 1

    while dq:
        x, y, z, cnt = dq.popleft()

        if x == n - 1 and y == m-1:
            answer = cnt
            return

        for m_x, m_y in move:
            n_x = x + m_x
            n_y = y + m_y

            if n_x in range(0, n) and n_y in range(0, m):

                # 벽이고 z=0이고 벽 뿌수고  온적없고 지금뿌술거
                if mapp[n_x][n_y] == 1 and z == 0:
                    dq.append((n_x, n_y, 1, cnt + 1))
                    checked[n_x][n_y][1] += 1

                # 갈 수 있는길이야 온적 없으면
                elif mapp[n_x][n_y] == 0 and checked[n_x][n_y][z] == 0:
                    dq.append((n_x, n_y, z, cnt + 1))
                    checked[n_x][n_y][z] += 1


checked = [[[0]*2 for _ in range(m)] for _ in range(n)]
bfs()


print(answer)
