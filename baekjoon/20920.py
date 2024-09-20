import sys
from collections import defaultdict

# 자주 나오는 단어
# 단어 길이 길면
# 오름차 순
n, m = map(int, sys.stdin.readline().split())  # m개 이상인 단어만 단어장에 추가
words = []
di = defaultdict(int)
for _ in range(n):
    x = sys.stdin.readline().rstrip()
    di[x] += 1
for word, cnt in di.items():
    if len(word) >= m:
        words.append((cnt,len(word),word))
words.sort(key=lambda x: (-x[0],-x[1],x[2]))

for _,_,word in words:
    print(word)
