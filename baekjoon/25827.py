import sys

n = int(sys.stdin.readline())
l = [0] * 86400
l2 = [0] * 86400
l3 = [0] * 86399
flag = False


def toSecond(t):
    answer = 0
    t = list(t)
    answer += int("".join(t[:2])) * 3600
    answer += int("".join(t[3:5])) * 60
    answer += int("".join(t[6:8]))

    return answer


for i in range(1, n + 1):
    num, start, end = map(str, sys.stdin.readline().split())

    if num == "1":
        second_start = toSecond(start)
        second_end = toSecond(end) - 1

        l[second_start] += 1
        l[second_end + 1] -= 1

    else:
        if not flag:
            cnt = 0
            for i in range(0, 86399):
                cnt += l[i]
                l2[i] = cnt
            l3[0] = l2[0]
            for i in range(1, 86399):
                l3[i] = l3[i - 1] + l2[i]
            flag = True

        second_start = toSecond(start)
        second_end = toSecond(end) - 1

        if second_start == 0:
            print(l3[second_end])
        else:
            print(l3[second_end] - l3[second_start - 1])
