import sys
from collections import defaultdict
n, k = map(int,sys.stdin.readline().split())
li = list(map(int,sys.stdin.readline().split()))
di = defaultdict(int)
start = 0
end = 1
answer = 0

di[li[start]] += 1
while start <= end and end < n:
    if di[li[end]] == k:
        di[li[start]] -= 1
        start += 1
    else:
        answer = max(answer, end- start + 1)
        di[li[end]] += 1
        end += 1
print(answer)