import sys
from unittest import result
f = sys.stdin.readline

n, m = map(int, f().split())

parent = [i for i in range(n+1)]
l = []
answer = 0
temp = 0


def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(m):
    a, b, c = map(int, f().split())
    l.append((c, a, b))

l.sort()

for i in l:
    if find_parent(i[1]) != find_parent(i[2]):
        union(i[1], i[2])
        answer += i[0]
        temp = i[0]

answer -= temp

print(answer)
