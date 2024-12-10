import sys

n = int(sys.stdin.readline())
lang = sys.stdin.readline().strip()
lang_size = len(lang)

if len(set(lang)) <= n:
    print(len(lang))
else:
    answer = 0
    start = 0
    end = 1
    s = set()
    while start < lang_size and end <= lang_size:
        now = lang[start:end]
        s = set(now)
        # print(lang[start:end], s)
        if len(s) > n:
            start += 1
        else:
            answer = max(answer, len(now))
            end += 1

    print(answer)
