from collections import defaultdict

def find_parents(parents,x):
    if parents[x] != x:
        parents[x] = find_parents(parents, parents[x])
    return parents[x]

def union(a,b,parents):
    a = find_parents(parents,a)
    b = find_parents(parents,b)
    
    if a < b:
        parents[b] = a
    else:
        parents[a] = b
        
def solution(n, wires):
    answer = 1e9
    
    for skip in wires:  # 전선 하나씩 끊어보기
        parents = [i for i in range(n+1)]
        
        for a, b in wires:
            if [a, b] == skip or [b, a] == skip:
                continue
            union(a, b, parents)
        
        # 각 노드마다 대표 부모 찾기
        for i in range(1, n+1):
            find_parents(parents, i)
        
        # 부모별로 노드 수 세기
        count = defaultdict(int)
        for i in range(1, n+1):
            count[parents[i]] += 1
        
        sizes = list(count.values())
        if len(sizes) == 2:
            answer = min(answer, abs(sizes[0] - sizes[1]))
    
    return answer