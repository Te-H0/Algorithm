import sys
from bisect import bisect_left

# 칭호, 캐릭터 수
n, m = map(int, sys.stdin.readline().split())
nick_li, standard = [], []
s = set()
for _ in range(n):
    nick, maximum = map(str, sys.stdin.readline().split())
    if int(maximum) not in s:
        s.add(int(maximum))
        nick_li.append(nick)
        standard.append(int(maximum))
answer = []
standard_size = len(standard)

for _ in range(m):
    x = int(sys.stdin.readline())
    print(nick_li[bisect_left(standard, x)])