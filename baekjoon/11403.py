import sys

f= sys.stdin.readline
INF = int(1e9)
n = int(f())

graph = []

for i in range(n):
    graph.append(list(map(int,f().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = INF

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

for i in range(n):
    for j in range(n):
        if graph[i][j] != INF:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()


