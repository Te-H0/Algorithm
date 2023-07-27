from cmath import sqrt
from math import ceil, floor
import sys
sys.setrecursionlimit(1000000)
f = sys.stdin.readline()

n = int(f)
result = False



def palindrome(n):
    result = False
    while not result:
        a= str(n)
        half = len(a)//2
        m = len(a)%2

        if m==0:
            result = a[:half] == a[len(a)-1:half-1:-1]
        else:
            result =  a[:half] == a[len(a)-1:half:-1]
        
        if result:
           result = prime_number(n) 
        
        if not result:
            n+=1
    return n

    

def prime_number(n):
    if n==1:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True



print(palindrome(n))
