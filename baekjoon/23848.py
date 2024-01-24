import sys, math

N = int(sys.stdin.readline())
flag = False
a, r, n, tmp = 0, 0, 0, 0

for i in range(int(math.sqrt(N)), 1, -1):  # r
    j = 3  # n
    tmp_sub = (i**j - 1) / (i - 1)
    last = i**2 
    cond = 2**3 -1
    cond_last = 4
    while cond <= N:  # n
        if N % tmp_sub == 0:
            a = int(N // tmp_sub)
            r = i
            n = j
            flag = True
            break
        j += 1
        last *=i
        tmp_sub += last
        cond_last*=2
        cond+=cond_last

if a == 0:
    print(-1)
else:
    print(n)
    for i in range(n):
        print(a * (r**i), end=" ")
