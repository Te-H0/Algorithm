import sys

NUMBER = [
    (1, 1, 1, 1, 1, 1, 0),
    (0, 1, 1, 0, 0, 0, 0),
    (1, 1, 0, 1, 1, 0, 1),
    (1, 1, 1, 1, 0, 0, 1),
    (0, 1, 1, 0, 0, 1, 1),
    (1, 0, 1, 1, 0, 1, 1),
    (1, 0, 1, 1, 1, 1, 1),
    (1, 1, 1, 0, 0, 0, 0),
    (1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 0, 1, 1),
]

diff = [[0] * 10 for _ in range(10)]

for i in range(10):
    for j in range(i, 10):
        cnt = 0
        if i != j:
            cnt = 0
            for k in range(7):
                cnt += NUMBER[i][k] ^ NUMBER[j][k]
        diff[i][j] = cnt
        diff[j][i] = cnt

# ~n층, k자리, ~p개 반전, x층
n, k, p, x = map(int, sys.stdin.readline().split())

str_x = "0" * (k - len(str(x))) + str(x)
answer = 0

# 1층부터 n층까지
for i in range(1, n + 1):
    if i == x:
        continue

    cnt = 0
    str_i = "0" * (k - len(str(i))) + str(i)

    # 자리 수 별로 반전 횟수 저장
    for j in range(k - 1, -1, -1):

        # 반전 추가
        if str_x[j] != str_i[j]:
            cnt += diff[int(str_x[j])][int(str_i[j])]

        # 반전 허용 이상이면 불가능
        if cnt > p:
            cnt = -1
            break

    if cnt != -1:
        answer += 1
print(answer)
