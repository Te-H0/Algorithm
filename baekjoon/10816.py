import sys
from bisect import bisect_left,bisect_right
from collections import Counter
from collections import defaultdict
n = int(sys.stdin.readline())
l = list(map(int, input().split()))
m = int(sys.stdin.readline())
find = list(map(int, input().split()))
l.sort()
for num in find:
    print(bisect_right(l,num)-bisect_left(l,num),end=" ")