import sys
from collections import deque
n = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))
answer = [0]
stack = []
stack.append((tower[0],1))

for i in range(1,n):
    while stack and stack[-1][0] < tower[i]:
        stack.pop()
    if not stack:
        answer.append(0)
    else:
        answer.append(stack[-1][1])
    stack.append((tower[i],i+1))
print(*answer)