import sys

l = list()

answer = 0
# n 접시, d 초밥 종류, k 연속 먹는 접시, c 쿠폰 번호
n, d, k, c = map(int, sys.stdin.readline().split())

for i in range(n):
    l.append(int(sys.stdin.readline()))

for i in range(n):
    s = set()
    if i + k > n:
        s.update(l[i:] + l[: i + k - n])
    else:
        s.update(l[i : i + k])

    s.add(c)
    answer = max(answer, len(s))
print(answer)
