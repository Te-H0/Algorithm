import sys
f = sys.stdin.readline

n, m = map(int, f().split())

l = [i for i in range(n+1)]
s=set()
def find_parent(x):
    if l[x] != x:
        l[x] = find_parent(l[x])
    return l[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        l[b] = a
    else:
        l[a] = b

for i in range(m):
    a, b = map(int, f().split())
    union_parent(a, b)


for i in range(1,n+1):
    find_parent(i)
    s.add(l[i])



print(len(s))
