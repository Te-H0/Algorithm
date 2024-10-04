import sys
from collections import deque
n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
visit = [False] * n
answer = -1
def bfs():
    global answer
    dq= deque()
    dq.append((0,0)) # idx, cnt
    visit[0] = True
    while dq:
        # print(dq)
        idx, cnt = dq.popleft()
        
        if idx == n-1:
            answer = cnt
            break
        for i in range(1,li[idx] + 1):
            if idx + i <n and not visit[idx+i]:
                dq.append((idx + i, cnt + 1))
                visit[idx+i] = True

bfs()
print(answer)