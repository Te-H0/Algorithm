import sys

x,y = map(int,sys.stdin.readline().split())

def gcd(x,y):
    if y>x:
        x,y = y,x
    
    while True:
        if y ==0:
           return x
        x,y= y, x%y

print((x+y)-(gcd(x,y)))