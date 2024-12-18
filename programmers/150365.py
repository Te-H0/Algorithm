import sys

sys.setrecursionlimit(10**6)
move = [((1, 0), "d"), ((0, -1), "l"), ((0, 1), "r"), ((-1, 0), "u")]

def dfs(n, m, x, y, r, c, k, a, b, s, cnt, answer):
    if k < cnt + abs(a - r) + abs(b - c):
        return "impossible"
    if cnt == k:
        if a == r and b == c:
            return s
        else:
            return "impossible"

    for mo in move:
        n_a = a + mo[0][0]
        n_b = b + mo[0][1]
        n_s = s + mo[1]

        if 1 <= n_a <= n and 1 <= n_b <= m:
            answer = dfs(n, m, x, y, r, c, k, n_a, n_b, n_s, cnt + 1, answer)
            if answer != "impossible":
                return answer
    return answer


def solution(n, m, x, y, r, c, k):
    if abs(x - r) + abs(y - c) > k or (k - (abs(x - r) + abs(y - c))) % 2 == 1:
        return "impossible"
    return dfs(n, m, x, y, r, c, k, x, y, "", 0, "impossible")