import sys

n = int(sys.stdin.readline())
s = set()

for i in range(n):
    word = sys.stdin.readline().strip()
    s.add(word)

l=list(s)
l.sort()
l.sort(key=len)

       

for i in l:
    print(i)
