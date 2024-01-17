import sys

n = int(sys.stdin.readline())

now = list(map(bool, (map(int, sys.stdin.readline().rstrip()))))
target = list(map(bool, (map(int, sys.stdin.readline().rstrip()))))


def switch(li):
    answer = 0

    for i in range(1, n - 1):
        if li[i - 1] != target[i - 1]:
            answer += 1
            li[i - 1] = not li[i - 1]
            li[i] = not li[i]
            li[i + 1] = not li[i + 1]

    if li[n - 2] != target[n - 2]:
        li[n - 2] = not li[n - 2]
        li[n - 1] = not li[n - 1]
        answer += 1

    if li == target:
        return answer
    else:
        return int(1e9)


tmp = now[:]

# 첫번째 버튼 생략
result = switch(tmp)

# 첫번째 버튼 누르고
now[0] = not now[0]
now[1] = not now[1]
result = min(switch(now) + 1, result)

if result == int(1e9):
    print(-1)
else:
    print(result)
