import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
deq = deque()
for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push_front":
        deq.appendleft(int(cmd[1]))
    elif cmd[0] == "push_back":
        deq.append(int(cmd[1]))
    elif cmd[0] == "pop_front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif cmd[0] == "pop_back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif cmd[0] == "size":
        print(len(deq))
    elif cmd[0] == "empty":
        if len(deq) == 0:
            print(1)
        else:
            print(0)

    elif cmd[0] == "front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif cmd[0] == "back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[len(deq)-1])
