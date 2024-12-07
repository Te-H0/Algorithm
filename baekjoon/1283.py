import sys

n = int(sys.stdin.readline())
li = [list(sys.stdin.readline().split()) for _ in range(n)]
check = []
s = set()

for i, l in enumerate(li):
    flag = False
    for j, word in enumerate(l):
        if word[0].lower() not in s:
            s.add(word[0].lower())
            li[i][j] = "[" + word[0] + "]" + word[1:]
            flag = True
            break
    if not flag:
        for j, word in enumerate(l):
            for k, w in enumerate(word):
                if w.lower() not in s:
                    s.add(w.lower())
                    li[i][j] = word[0:k] + "[" + w + "]" + word[k + 1 :]
                    flag = True
                    break
            if flag:
                break
for l in li:
    print(*l)
