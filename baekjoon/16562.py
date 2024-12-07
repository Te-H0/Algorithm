import sys
sys.setrecursionlimit(100000)
# 학생 수, 친구관계 수, 돈
n, m, k = map(int, sys.stdin.readline().split())

tmp_friend_fee = list(map(int, sys.stdin.readline().split()))
friend_fee = []
for i in range(1, n + 1):
    friend_fee.append((tmp_friend_fee[i - 1], i))
friend_fee.sort()
parents = [-1] * (n+1)
s = set()
answer = 0
count = 0

def find_parent(x):
    if parents[x] > 0:
        return find_parent(parents[x])
    return x


def uion_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)


    if a!=b:
        if a > b:
            parents[b] += parents[a]
            parents[a] = b
        else:
            parents[a] += parents[b]
            parents[b] = a


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    uion_parent(a, b)

for fee, num in friend_fee:
    p = find_parent(num)
    if p not in s:
        answer += fee

        if k - answer <0:
            print("Oh no")
            break
        else:
            s.add(p)
            count += -parents[p]
            if count == n:
                print(answer)
                break
