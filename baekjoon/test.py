import sys
f= sys.stdin.readline

temp = []
for i in range(3):
    temp.append(list(map(int,f().split())))

print(temp)