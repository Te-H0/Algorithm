import sys
from collections import defaultdict, deque

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

di = defaultdict(int)
map = ""
for _ in range(3):
    map += "".join(sys.stdin.readline().split())


def bfs():
    dq = deque()
    dq.append((map, map.find("0")))

    while dq:
        x, idx = dq.popleft()

        if x == "123456780":
            return di[x]

        a = idx // 3
        b = idx % 3
        for m_a, m_b in move:
            n_a = a + m_a
            n_b = b + m_b
            n_idx = n_a * 3 + n_b
            if 0 <= n_a <= 2 and 0 <= n_b <= 2:
                tmp = list(x)
                tmp[idx], tmp[n_idx] = tmp[n_idx], tmp[idx]
                tmp2 = "".join(tmp)
                if tmp2 not in di:
                    di[tmp2] += di[x] + 1
                    dq.append((tmp2, tmp2.find("0")))
    return -1


print(bfs())
