from bisect import bisect_left, bisect_right, insort,bisect

l = [1, 2, 2, 4, 4, 5]

a = bisect(l, 2)
d = bisect_right(l, 2)
b = bisect_left(l, 2)
e = bisect_left(l, 3)
c = bisect_right(l, 3)
insort(l, 3)
print(l)
