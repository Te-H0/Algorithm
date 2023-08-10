# 149
import sys

move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
r, c = map(int, sys.stdin.readline().split())

graph = [list(sys.stdin.readline().rstrip()) for i in range(r)]
counter = set()
counter.add(graph[0][0])
answer =0


def sol(x, y, cnt):
    global answer
    
    answer = max(cnt,answer)
    for i in range(4):
        nx = x+move[i][0]
        ny = y+move[i][1]

        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in counter:
            counter.add(graph[nx][ny])
            answer = sol(nx, ny, cnt+1)
            counter.remove(graph[nx][ny])

    return max(cnt, answer)

sol(0, 0, 1)
print(answer)
