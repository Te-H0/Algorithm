import sys
from collections import deque
f = sys.stdin.readline

l, c = map(int, f().split())

li = list(map(str, f().split()))
password = []
tmp_vowel = []

consonant = []


for i in li:
    if i in ['a', 'e', 'i', 'o', 'u']:
        tmp_vowel.append(i)

len_tmp_vowel = len(tmp_vowel)

vowel = [[]for i in range(c-1)]


def pick_consonant(idx, tmp):
    global c, l
    if len(tmp) >= 2 and len(tmp) <= l-1:
        consonant.append(''.join(tmp))
    if len(tmp) == l-1:
        return
    for i in range(idx, c):
        if li[i] not in tmp_vowel:
            tmp.append(li[i])
            pick_consonant(i+1, tmp)
            tmp.pop()

# n ==> 몇개 고를건지


def pick_vowel(n, idx, tmp):
    if len(tmp) == n:
        vowel[n].append(''.join(tmp))
        return

    for i in range(idx, len_tmp_vowel):
        tmp.append(tmp_vowel[i])
        pick_vowel(n, i+1, tmp)
        tmp.pop()


for i in range(1, min(len_tmp_vowel, l-1)+1):
    pick_vowel(i, 0, deque())

pick_consonant(0, deque())

for x in consonant:
    a = len(x)
    for y in vowel[l-a]:
        temp = list(x+y)
        temp.sort()
        temp2 = ''.join(temp)
        password.append(temp2)


password.sort()
for i in password:
    print(i)
