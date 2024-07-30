import sys,math

n = int(sys.stdin.readline())
total = math.floor(math.sqrt(1500000))
prime = [True] * 1500000
prime[1] = False

for i in range(2,total):
    if prime[i]:
        j=2
        while i*j < 1500000:
            prime[i*j] = False
            j+=1

def is_palindrome(x):
    str_x = str(x)
    size=len(str_x)
    if size == 1:
        return True    
    return str_x[:size//2] == str_x[-1:-(size//2+1):-1]

for i in range(n,1500000):
    if prime[i]:
        if is_palindrome(i):
            print(i)
            break