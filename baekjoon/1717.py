import sys
sys.setrecursionlimit(100000)
n,m = map(int, sys.stdin.readline().split())

parent = [i for i in range(n+1)] 

def find_parent(x):
    if parent[x]!=x:
        parent[x] = find_parent(parent[x])
    return parent[x]
def union(x,y):
    p_x = find_parent(x)
    p_y = find_parent(y)
    
    if p_y > p_x :
        parent[p_y] = p_x
    else:
        parent[p_x] = p_y
    
for _ in range(m):
    x,y,z = map(int, sys.stdin.readline().split())
    
    if x == 0:
        union(y,z)
    else:
        if find_parent(y)==find_parent(z):
            print("YES")
        else:
            print("NO")