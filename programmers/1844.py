from collections import deque
move = [(-1,0),(1,0),(0,-1),(0,1)]
def bfs(maps):
    dq = deque()
    dq.append((0,0,1))
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    while dq:
        i,j,cnt = dq.popleft()
        if i == n - 1 and j == m - 1:
            return cnt
        
        for m_i, m_j in move:
            n_i = i + m_i
            n_j = j + m_j
            
            if n_i in range(n) and n_j in range(m) and not visited[n_i][n_j] and maps[n_i][n_j]:
                dq.append((n_i,n_j,cnt+1))
                visited[n_i][n_j] = True
    return -1

def solution(maps):
    return bfs(maps)