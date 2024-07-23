import sys

n = int(sys.stdin.readline())
l = [int(sys.stdin.readline().strip()) for _ in range(n)]
reverse_l = l[::-1]
answer = 0

pre = reverse_l[0]
for i in range(1,n):
    if reverse_l[i]>=pre:
        answer += reverse_l[i] - (pre-1)
        pre = (pre-1)
    else:
        pre=reverse_l[i]
print(answer)
