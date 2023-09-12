import sys

n = int(sys.stdin.readline())
cnt = 0
stack = []
top = 0
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())

    while top > y:
        stack.pop()
        cnt += 1

        if len(stack) == 0:
            top = 0
        else:
            top = stack[-1]

    if top < y:
        stack.append(y)
        top = stack[-1]

cnt += len(stack)
print(cnt)
