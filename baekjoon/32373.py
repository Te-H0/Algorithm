import sys

n, k = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

answer = "Yes"
if li != [i for i in range(n)]:
    for i in range(k):
        # print(f"i => {i}")
        for j in range(i, n, k):
            # print(f"j => {j}")
            # print(li[j])
            if i != li[j] % k:
                answer = "No"
                break
        if answer == "No":
            break

print(answer)

# 8 5
# 0 : 2 0
# 1 : 1 4
# 2 : 6 5
# 3 : 3
# 4 : 4
# 5 : 0
# 6 :

# 8 2
# 0 : 0 2 4 6
# 1 : 1 3 5 7
