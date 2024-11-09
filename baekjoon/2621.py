import sys
from collections import defaultdict

# R, B, Y, G
color_cnt = []
num_cnt = [0] * 10
num_li = []
di = defaultdict(list)

for _ in range(5):
    a, b = map(str, sys.stdin.readline().split())
    di[a].append(int(b))
    num_cnt[int(b)] += 1
    num_li.append(int(b))

for x in ('R', 'B', 'Y', 'G'):
    color_cnt.append(len(di[x]))
    
def idx_to_color(idx):
    if idx == 0:
        return 'R'
    elif idx == 1:
        return 'B'
    elif idx ==2:
        return 'Y'
    elif idx ==3:
        return 'G'

def is_continous(li):
    li.sort()
    # print(li)
    pre = li[0]
    for l in li[1:]:
        if l!=pre + 1:
            return False
        pre = l
    return True

if 5 in color_cnt and is_continous(di[idx_to_color(color_cnt.index(5))]):
    print(900 + di[idx_to_color(color_cnt.index(5))][-1])
elif 4 in num_cnt:
    print(800 + num_cnt.index(4))
elif 3 in num_cnt and 2 in num_cnt:
    print(num_cnt.index(3) * 10 + num_cnt.index(2) + 700)
elif 5 in color_cnt:
    print(max(di[idx_to_color(color_cnt.index(5))]) + 600)
elif is_continous(num_li):
    print(num_li[-1] + 500)
elif 3 in num_cnt:
    print(400 + num_cnt.index(3))
elif num_cnt.count(2) == 2:
    pre = 0
    for i in range(1,10):
        if num_cnt[i] == 2:
            if pre == 0:
                pre = i
                continue
            else:
                print(i*10 + pre + 300)
                break
elif 2 in num_cnt:
    print(num_cnt.index(2) + 200)
else:
    print(max(num_li) + 100)


