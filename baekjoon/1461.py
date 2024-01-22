import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
li.sort()
answer = 0
flag = False  # false면 절댓값 큰 값이 negative쪽에, ture면 positive쪽에
negative_dq = deque()
positive_dq = deque()


while li:
    x = li.pop()
    if x > 0:
        positive_dq.appendleft(x)
    else:
        negative_dq.appendleft(x)

if len(negative_dq) == 0 or (
    len(positive_dq) != 0 and positive_dq[-1] > -negative_dq[0]
):
    flag = True

p_l = len(positive_dq)
n_l = len(negative_dq)
if flag:  # 제일 큰값이 positive에 있을 때
    max = 0
    min = 0
    while p_l >= m:
        x = positive_dq.pop()
        if max == 0:
            max = x
            answer += max
        else:
            max = x
            answer += max * 2
        for _ in range(m - 1):
            positive_dq.pop()
        p_l -= m

    if positive_dq:
        if max == 0:
            answer += positive_dq[-1]
        else:
            answer += positive_dq[-1] * 2

    while n_l >= m:
        x = negative_dq.popleft()
        min = x
        answer += -min * 2
        for _ in range(m - 1):
            negative_dq.popleft()
        n_l -= m
    if negative_dq:
        answer += -negative_dq[0] * 2
else:
    max = 0
    min = 0
    while n_l >= m:
        x = negative_dq.popleft()
        if min == 0:
            min = x
            answer += -min
        else:
            min = x
            answer += -min * 2
        for _ in range(m - 1):
            negative_dq.popleft()
        n_l -= m
    if negative_dq:
        if min == 0:
            answer += -negative_dq[0]
        else:
            answer += -negative_dq[0] * 2
    while p_l >= m:
        x = positive_dq.pop()
        max = x
        answer += max * 2
        for _ in range(m - 1):
            positive_dq.pop()
        p_l -= m
    if positive_dq:
        answer += positive_dq[-1] * 2


print(answer)
