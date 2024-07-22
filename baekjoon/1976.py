import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
plan = list(map(int, sys.stdin.readline().split()))
answer = "YES"
INF = int(1e9)
parent = [i for i in range(n)]

def union_parent(i,j):
    p_i = find_parent(i)
    p_j = find_parent(j)
    
    if p_i > p_j:
        parent[p_i] = p_j
    else:
        parent[p_j] = p_i

def find_parent(x):
    if x!=parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

for i in range(n):
    for j in range(n):
        if graph[i][j]:
            union_parent(i,j)

p = parent[plan.pop(0)-1]
for x in plan:
    if parent[x-1] != p:
        answer= "NO"
        break

print(answer)

    
    
# import sys

# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())
# graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# plan = list(map(int, sys.stdin.readline().split()))
# answer = "YES"
# INF = int(1e9)

# for i in range(n):
#     for j in range(n):
#         if i != j and not graph[i][j]:
#             graph[i][j] = INF

# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# pre = plan.pop(0)
# for p in plan:
#     if graph[pre-1][p-1] == INF:
#         answer = "NO"
#         break
#     pre = p

# print(answer)

