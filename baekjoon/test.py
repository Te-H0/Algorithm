import sys

l = [False for i in range(100000+1)]
l[100000] = True
print(l)
