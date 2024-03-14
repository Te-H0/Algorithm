import sys

cnt_li = [0] * 13
graph = [[] for _ in range(13)]

for _ in range(12):
    a, b = map(int, sys.stdin.readline().split())
    cnt_li[a] += 1
    cnt_li[b] += 1

    graph[a].append(b)
    graph[b].append(a)
for i in range(1, 13):
    if cnt_li[i] == 3:
        s = set()
        for j in graph[i]:
            if (cnt_li[j] in s) or (cnt_li[j] not in range(1, 4)):
                break
            else:
                s.add(cnt_li[j])
        if len(s) == 3:
            print(i)
            break
