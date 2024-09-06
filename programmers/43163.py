from collections import deque


def diff_counter(x, y):  # 두 단어의 차이 나는 글자 수
    result = -1
    size = len(x)
    if size != len(y):
        return result

    cnt = 0
    idx = 0
    while idx < size and cnt <= 1:  # 2글자 이상 차이나면 종료
        if x[idx] != y[idx]:
            cnt += 1
        idx += 1

    return cnt


def bfs(begin, target, words, check):
    answer = 0
    flag = False
    dq = deque()
    dq.append((begin, 0))  # 단어, 카운트

    while dq and not flag:
        w, cnt = dq.popleft()
        for i in range(len(words)):
            y = words[i]
            if (
                not check[i] and diff_counter(w, y) == 1
            ):  # 방문 안했고 글자 수 차이 1개면
                if y == target:  # target이면?
                    answer = cnt + 1
                    flag = True
                    break
                dq.append((y, cnt + 1))
                check[i] = True
    return answer


def solution(begin, target, words):
    if target not in words:
        return 0
    check = [False] * len(words)
    answer = bfs(begin, target, words, check)

    return answer
