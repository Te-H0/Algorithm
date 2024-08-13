import sys

n, k = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
answer = 0
end = 1
odd = 0
cnt = 0

if li[0] % 2 == 0:  # 짝수면
    cnt += 1
else:
    odd += 1
    
for i in range(n):
    while odd <= k and end < n:
        if li[end] % 2 == 0:  # 짝수면
            cnt += 1
        else:
            odd += 1
        end += 1
    answer = max(cnt, answer)
    if li[i] % 2 == 1:
        odd -= 1
    else:
        cnt -= 1

print(answer)
