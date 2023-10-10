import sys
import math
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())
li = [0]
tmp = list(map(int, sys.stdin.readline().split()))
di = defaultdict(int)
answer = 0

for i in range(1, n+1):
    x = (li[i-1] + tmp[i-1]) % m
    di[x] += 1
    li.append(x)

mod_li = list(di.items())

for m_l in mod_li:
    if m_l[0] == 0:
        answer += m_l[1]
    if m_l[1] >= 2:
        answer += math.comb(m_l[1], 2)

print(answer)
