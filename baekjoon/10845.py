from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())
q = deque()

for i in range(n):
    cmd =sys.stdin.readline().split()

    if cmd[0]=='push':
        q.appendleft(int(cmd[1]))
    elif cmd[0] == 'pop':
        if len(q) != 0:
            print(q.pop())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[len(q)-1])
    else:
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
