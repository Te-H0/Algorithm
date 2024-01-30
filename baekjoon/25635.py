import sys
from queue import PriorityQueue

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

li.sort()

m = li[-1]
total = sum(li[: n - 1])

if m <= total:  # 가장 큰게 나머지 합보다 작으면 다 써 같아도 다써
    print(sum(li))
else:  # 가장 큰게 더 크면? ...... 나머지꺼 2배 하고 가장 큰거 에서 한개?
    print(total * 2 + 1)
