import sys
import heapq

n = int(sys.stdin.readline())
hq = []

for _ in range(n):
    heapq.heappush(hq, int(sys.stdin.readline()))

answer = 0

if n == 1:
    print(answer)
else:
    while len(hq) != 1:
        x1 = heapq.heappop(hq)
        x2 = heapq.heappop(hq)

        tmp = x1+x2
        answer += tmp
        heapq.heappush(hq, tmp)

    print(answer)
