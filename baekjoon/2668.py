import sys
n = int(sys.stdin.readline())
li = [0]*(n+1)
visited = [False] * (n+1)
answer = []
for i in range(1, n+1):
    x = int(sys.stdin.readline().rstrip())
    li[i] = x


def dfs(idx, top, bottom):
    checked[idx] = True
    top.add(idx)
    bottom.add(li[idx])

    if top == bottom:
        answer.extend(list(top))
        return

    l = li[idx]
    if not checked[l]:
        dfs(l, top.copy(), bottom.copy())


for i in range(1, n+1):
    if not visited[i]:
        checked = [False]*(n+1)
        dfs(i, set(), set())

answer = list(set(answer))
answer.sort()
print(len(answer))
for a in answer:
    print(a)

# 7
# 3
# 1
# 1
# 5
# 5
# 4
# 6
