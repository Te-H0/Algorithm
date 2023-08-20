from re import X
import sys
from collections import deque
s = str(sys.stdin.readline().rstrip())
t = str(sys.stdin.readline().rstrip())


def bfs(x):
    dq = deque()
    s = set()
    max = len(t)
    a_c = t.count("A")
    b_c = t.count("B")
    dq.append(x)
    s.add(x)

    while dq:
        word = dq.popleft()
        print(word, "지금 word")
        if word == t:
            return 1
        
        if len(word) < max:
            if word+"A" not in s and a_c > word.count("A") and (word in t or word[::-1] in t):
                dq.append(word+"A")
                s.add(word+"A")
            if (word+"B")[::-1] not in s and b_c > word.count("B") and (word in t or word[::-1] in t):
                dq.append((word+"B")[::-1])
                s.add((word+"B")[::-1])
    return 0


print(bfs(s))
