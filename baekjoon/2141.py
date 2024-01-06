import sys

n = int(sys.stdin.readline())
li = []
total = 0
cnt = 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    li.append((a,b))
    total += b
li.sort(key= lambda x: x[0])
half = total / 2

for idx, value in li:
    cnt += value
    if half <= cnt:
        print(idx)
        break
