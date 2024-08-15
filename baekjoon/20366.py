import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
li.sort()

answer = int(1e10)

for i in range(n):
    for j in range(i+3,n):
        snow_man1= li[i]+li[j]
        
        start = i+1
        end = j-1
        while start < end:
            snow_man2 = li[start] + li[end]
            diff = snow_man1 - snow_man2
            if diff < 0:
                diff *= -1
            answer = min(diff, answer)

            if snow_man1 > snow_man2:
                start += 1
            elif snow_man1 < snow_man2:
                end -= 1
            else:
                break
        
    if answer == 0:
        break

print(answer)