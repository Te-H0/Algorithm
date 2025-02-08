import sys
sys.setrecursionlimit(1000000)
def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    
    return parents[x]

def union_parents(a,b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a==b:
        return False
    else:
        if a < b:
            parents[b] = a
        else:
            parents[a] = b
        return True
v,e = map(int,sys.stdin.readline().split())
li = []
parents= [i for i in range(v)]
for _ in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    li.append((c,a-1,b-1))

li.sort()

answer = 0
for cost, a, b in li:
    if find_parent(a) != find_parent(b):
        union_parents(a,b)
        answer += cost

print(answer)