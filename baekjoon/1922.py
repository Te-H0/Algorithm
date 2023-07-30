import sys
f = sys.stdin.readline


def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n = int(f())
m = int(f())

parent = [i for i in range(n+1)]
l = list()
result = 0

for i in range(m):
    a, b, cost = map(int, f().split())
    l.append((cost, a, b))

l.sort()

for x in l:
    if not(find_parent(parent, x[1]) == find_parent(parent, x[2])):
        union_parent(parent, x[1], x[2])
        result += x[0]

print(result)
