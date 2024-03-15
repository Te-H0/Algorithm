import sys

n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n)]
answer = 0
flag = False


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a_p = find_parent(a)
    b_p = find_parent(b)
    if a_p == b_p:
        return True

    if a_p > b_p:
        parent[a_p] = b_p
    else:
        parent[b_p] = a_p


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    answer += 1

    if union(a, b):
        flag = True
        break
if flag:
    print(answer)
else:
    print(0)

# 6 5
# 0 1
# 1 2
# 1 3
# 0 3
# 4 5
