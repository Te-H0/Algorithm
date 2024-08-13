import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

li.sort()

l_idx = 0
r_idx = n - 1
answer = 0
while l_idx < r_idx:
    sum = li[l_idx] + li[r_idx]
    if sum == x:
        answer += 1
        l_idx += 1
        r_idx -=1
    elif sum > x:
        r_idx -=1
    else:
        l_idx +=1

print(answer)
    