import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):

    n = int(sys.stdin.readline())
    parent = [0] * (n + 1)
    
    for _ in range(n - 1):
        x, y = map(int, sys.stdin.readline().split())
        parent[y] = x  # parent[자식] = 부모
    a, b = map(int, sys.stdin.readline().split())
    
    tmp_a, tmp_b = a,b
    p_a = [a] # 자기 자신 집어넣고 해야 예외 처리 줄음
    p_b = [b]
    
    while parent[tmp_a]: # a의 부모 담기 [,,,,root]
        p_a.append(parent[tmp_a])
        tmp_a = parent[tmp_a]

 
    while parent[tmp_b]: # b의 부모 담기 [,,,,root]
        p_b.append(parent[tmp_b])
        tmp_b = parent[tmp_b]

    x = p_a.pop()
    y = p_b.pop()
    root = x # 무슨 일이 있어도 첫번째는 root
    pre = root
    
    while p_a and p_b: # 역순으로 루트부터 비교해서 달라지기 직전의 노드가 부모
        x = p_a.pop()
        y = p_b.pop()
            
        if x == y:
            pre = x
        else:
            break
    print(pre)
