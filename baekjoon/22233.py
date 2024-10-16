import sys

n, m = map(int, sys.stdin.readline().split())
s = set()
for _ in range(n):
    keyword = sys.stdin.readline().rstrip()
    s.add(keyword)

for _ in range(m):
    li = sys.stdin.readline().rstrip()
    li = li.split(',')
    
    for l in li:
        if l in s:
            s.remove(l)
    
    print(len(s))
