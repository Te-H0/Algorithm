import sys
from bisect import bisect_left, bisect_right

n, k = map(int, sys.stdin.readline().split())
gift = list(map(int, sys.stdin.readline().split()))
box = list(map(int, sys.stdin.readline().split()))
received = list(map(int, sys.stdin.readline().split()))
check = [True] * n
gift.sort()
box.sort()
li = [[] for _ in range(n)]

for i in range(n):
    if box[0] >= gift[i]:
        li[0].append((i, gift[i]))
    else:
        break

for i in range(1, n):
    pre_box = li[i - 1][:]
    last_idx = pre_box[-1][0]
    now_box = []

    for j in range(last_idx + 1, n):
        if box[i] >= gift[j]:
            now_box.append((j, gift[j]))
        else:
            break

    if not now_box:
        li[i] = pre_box[:]
        li[i].sort()
    else:
        li[i] = now_box[:]
        li[i].sort()

# print(li)

for r in received:
    x = bisect_left(box, r)

    for l in li[x]:
        if check[l[0]]:
            check[l[0]] = False
            print(f"{gift[l[0]]} !!!")
            break

for i in range(n - 1, -1, -1):
    if check[i]:

        print(gift[i])
        break

    # # print(x1, x2)
    # for idx in range(x1, x2):
    #     if li[idx]:
    #         li[idx].pop(0)
    #     # print(li)
    # # print("--------")

# li.reverse()
# for l in li:
#     if l:
#         print(l[-1][1])
#         break
# li.reverse()
# print(li)


# 선물이 들어갈 수 있는 가장 작은 박스에 선물 넣기

# 선물 크기 -  1 3 5 7 9 11 13
# 상자 크기 -  1 5 6 9 9 13 13


#  상자 담을 수 있는 거
# 1 - 1

# 5 - 1  3 5
# 6 - 1  3 5

# 9  - 1  3 5  7 9
# 9  - 1  3 5  7 9
# 13 - 1  3 5  7 9   11 13
# 13 - 1  3 5  7 9   11 13

# 13 9 13
# 13 9  11
