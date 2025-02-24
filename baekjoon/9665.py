import sys
from collections import deque

n = int(sys.stdin.readline())
tmp = ["SK", "CY"]
dp = [-1] * (n + 1)
print(tmp[n % 2 - 1])
