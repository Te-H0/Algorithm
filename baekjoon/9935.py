import sys
from collections import deque

x = list(sys.stdin.readline().rstrip())
bomb = list(sys.stdin.readline().rstrip())
bomb_size = len(bomb)
stack = []

for i in range(len(x)):
    stack.append(x[i])
    if stack[-bomb_size:] == bomb:
        for _ in range(bomb_size):
            stack.pop()
answer = ''.join(stack)
if answer == "":
    print("FRULA")
else:
    print(answer)
