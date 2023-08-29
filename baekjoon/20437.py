import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    w = sys.stdin.readline().rstrip()
    k = int(sys.stdin.readline().rstrip())

    answer = [100001, -1]
    c = Counter(w)
    s = set(w)
    idx_l = []

    for word in s:
        if c[word] >= k:
            tmp_l = []
            start = -1
            for _ in range(c[word]):
                find_idx = w[start+1:].index(word) + start+1
                tmp_l.append(find_idx)
                start = find_idx
            idx_l.append(tmp_l)

    for idx in idx_l:
        for i in range(len(idx)-k+1):
            n_len = idx[i+k-1] - idx[i]
            answer[0] = min(answer[0], n_len+1)
            answer[1] = max(answer[1], n_len+1)

    if answer[1] == -1:
        print(-1)
    else:
        for result in answer:
            print(result, end=" ")
        print()
