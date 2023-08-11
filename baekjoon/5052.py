import sys

t = int(sys.stdin.readline())

for i in range(t):
    result ="YES"
    n = int(sys.stdin.readline())
    l = []
    for j in range(n):
        l.append(sys.stdin.readline().rstrip())

    l.sort()

    for j in range(n-1):
        if l[j] == l[j+1][:len(l[j])]:
            result = "NO"
            break
    
    print(result)

# 2
# 3
# 911
# 97625999
# 91125426
# 5
# 113
# 12340
# 123440
# 12345
# 98346

    
