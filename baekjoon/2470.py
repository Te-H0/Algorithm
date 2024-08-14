import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
answer = [0, n - 1]
li.sort()

left = 0
right = n - 1
tmp = li[left] + li[right]
zero = li[left] + li[right]  # 0에 가까운 수

while right - left > 1 and zero != 0:
    if tmp > 0:
        right -= 1
    elif tmp < 0:
        left += 1
    tmp = li[left] + li[right]
    
    if zero**2 > tmp**2: # 음/양 수 구분 없이 0에 가까운 수 찾기 위해 제곱
        zero = tmp
        answer[0] = left
        answer[1] = right

print(li[answer[0]], li[answer[1]])
