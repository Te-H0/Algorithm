from re import T
from sqlite3 import connect
import sys
from itertools import product
c = int(sys.stdin.readline())

for _ in range(c):
    n = int(sys.stdin.readline())
    l = []
    answer = []
    for i in range(2*n-1):
        if i % 2:
            l.append('')
        else:
            l.append(str(int((i+1)-i/2)))

    # n-1개의 부호 필요함.
    oper = [['+', '-', ''] for _ in range(n-1)]
    oper_list = list(product(*oper))

    for ol in oper_list:
        tmp_li = l[:]
        idx = 1
        for o in ol:
            tmp_li[idx] = o
            idx += 2

        sum = eval(''.join(tmp_li))
        if sum == 0:
            answer.append(tmp_li)
    answer.sort()

    for ans in answer:
        for a in ans:
            if a == '':
                print(" ", end='')
            else:
                print(a, end='')
        print()
    print()
