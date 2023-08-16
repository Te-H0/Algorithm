import sys

while True:
    try:
        x = (int(sys.stdin.readline()))*10000000
        n = int(sys.stdin.readline())
        lego = []
        answer = 0
        for i in range(n):
            lego.append(int(sys.stdin.readline()))

        lego.sort()

        if n == 0:
            print("danger")

        else:
            i = 0
            j = n-1 
            while i<j:
                tmp = lego[i] + lego[j]
                if tmp == x:
                    answer = lego[i]
                    break
                elif tmp> x:
                    j-=1
                else:
                    i+=1
            if answer == 0:
                print("danger")
            else:
                print("yes", answer, x-answer)
    except:
        break
