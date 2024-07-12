import sys

n, m = map(int, sys.stdin.readline().split())
answer = []
l = []
check = [False] * n

def dfs(cnt):
    if cnt == m:
        answer.append(l[:])
        return

    for i in range(1, n+1):
        if not check[i-1]:
            l.append(i)
            check[i-1] = True
            dfs(cnt + 1)
            l.pop()
            check[i-1] = False

dfs(0)
for i in answer:
    print(*i)