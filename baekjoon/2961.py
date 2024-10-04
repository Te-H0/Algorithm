import sys
from itertools import combinations
# 신맛 : 재료의 신맛의 곱
# 쓴맛 : 재료의 쓴맛의 합
# 1 2 3 4
# 6 7 8 9

n = int(sys.stdin.readline())
sour = []
bitter = []

for _ in range(n):
    s,b = map(int,sys.stdin.readline().split())
    sour.append(s)
    bitter.append(b)
    
combi = []
for j in range(1, n + 1):
    combi += list(combinations([i for i in range(n)], j))
# print(combi)
answer = int(1e9)

for co in combi:
    sour_taste = 1
    bitter_taste = 0
    for c in co:
        sour_taste *= sour[c]
        bitter_taste += bitter[c]
    answer = min(answer, abs(sour_taste - bitter_taste))

print(answer)

