import sys

n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))

answer = 0
check = [False] * 100001
start,end = 0,0

while start !=n and end != n:
    if not check[li[end]]:
        check[li[end]] = True
        end += 1
        answer += (end - start)
    else:
        check[li[start]] = False
        start += 1
print(answer)