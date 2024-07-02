import sys
from collections import deque

move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
n, m = map(int, sys.stdin.readline().split())
check = [[0] * m for _ in range(n)]
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

day = 1
dq = deque()
daily = [(0, 0)]
check[0][0] = day

while daily:
    day += 1
    dq = deque(daily)
    daily = []
    while dq:
        x, y = dq.pop()

        for m_x, m_y in move:
            if (
                x + m_x in range(n)
                and y + m_y in range(m)
                and check[x + m_x][y + m_y] == 0
                and graph[x + m_x][y + m_y] == 1
            ):
                check[x + m_x][y + m_y] = day
                if x + m_x == n - 1 and y + m_y == m - 1:
                    break
                else:
                    daily.append((x + m_x, y + m_y))
        if check[n - 1][m - 1] != 0: # 이거 안했더니 시간초과
            daily = []
            break

print(check[n - 1][m - 1])
