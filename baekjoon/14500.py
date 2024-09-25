import sys

width_blank = [
    [(0, 0), (0, 1)],
    [(0, 1), (0, 2)],
    [(1, 0), (1, 1)],
    [(1, 1), (1, 2)],
    [(0, 0), (1, 2)],
    [(0, 2), (1, 0)],
    [(0, 0), (0, 2)],
    [(1, 0), (1, 2)],
]
height_blank = [
    [(0, 0), (1, 0)],
    [(0, 1), (1, 1)],
    [(1, 0), (2, 0)],
    [(1, 1), (2, 1)],
    [(0, 0), (2, 1)],
    [(0, 1), (2, 0)],
    [(0, 0), (2, 0)],
    [(0, 1), (2, 1)],
]
n, m = map(int, sys.stdin.readline().split())

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(m):
        # 막대 가로
        if j + 4 <= m:
            answer = max(answer, sum(paper[i][j : j + 4]))

        # 막대 세로
        if i + 4 <= n:
            tmp = paper[i][j]
            for k in range(1, 4):
                tmp += paper[i + k][j]
            answer = max(answer, tmp)

        # 정사각형
        if i + 2 <= n and j + 2 <= m:
            answer = max(
                answer, sum(paper[i][j : j + 2]) + paper[i + 1][j] + paper[i + 1][j + 1]
            )

        # 2x3 직사각형 가로
        if i + 2 <= n and j + 3 <= m:
            tmp_sum = sum(paper[i][j : j + 3]) + sum(paper[i + 1][j : j + 3])
            tmp_li = []

            for w_b in width_blank:
                tmp_li.append(
                    tmp_sum
                    - paper[i + w_b[0][0]][j + w_b[0][1]]
                    - paper[i + w_b[1][0]][j + w_b[1][1]]
                )
            answer = max(answer, max(tmp_li))

        # 3x2 직사각형 세로
        if i + 3 <= n and j + 2 <= m:

            tmp_sum = (
                sum(paper[i][j : j + 2])
                + sum(paper[i + 1][j : j + 2])
                + sum(paper[i + 2][j : j + 2])
            )
            tmp_li = []

            for h_b in height_blank:
                tmp_li.append(
                    tmp_sum
                    - paper[i + h_b[0][0]][j + h_b[0][1]]
                    - paper[i + h_b[1][0]][j + h_b[1][1]]
                )
            answer = max(answer, max(tmp_li))
            if answer == 25:
                print(i, j, 5)
print(answer)
