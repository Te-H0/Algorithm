import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
bus = [[int(1e9)] * n for _ in range(n)]

for i in range(n):
    bus[i][i] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    bus[a - 1][b - 1] = min(c, bus[a - 1][b - 1])

for k in range(n):
    for i in range(n):
        for j in range(n):
            bus[i][j] = min(bus[i][j], bus[i][k] + bus[k][j])

for i in range(n):
    for j in range(n):
        if bus[i][j] ==int(1e9):
            print(0, end=' ')
        else:
            print(bus[i][j], end=" ")
    print()
