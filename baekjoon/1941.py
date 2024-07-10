import sys
from collections import deque

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
graph = []
answer = 0

def dfs(idx, cnt, dasom_cnt):
    global answer
    if cnt == 7:
        if dasom_cnt >= 4 and is_seven_princess():
            answer += 1
        return
    for i in range(idx, 25):
        x = i // 5
        y = i % 5
        if not check[x][y]:
            check[x][y] = True
            dfs(i + 1, cnt + 1, dasom_cnt + int(graph[x][y] == "S"))
            check[x][y] = False

def is_seven_princess():
    dq = deque()
    visit = [[False] * 5 for _ in range(5)]
    for i in range(25):
        if check[i // 5][i % 5]:
            dq.append((i // 5, i % 5))
            visit[i // 5][i % 5] = True
            break

    cnt = 1
    while dq:
        x, y = dq.popleft()
        for m_x, m_y in move:
            n_x = x + m_x
            n_y = y + m_y
            if 0 <= n_x < 5 and 0 <= n_y < 5 and check[n_x][n_y] and not visit[n_x][n_y]:
                visit[n_x][n_y] = True
                cnt += 1
                dq.append((n_x, n_y))

    return cnt == 7

for _ in range(5):
    graph.append(list(sys.stdin.readline().strip()))

check = [[False] * 5 for _ in range(5)]
dfs(0, 0, 0)

print(answer)
