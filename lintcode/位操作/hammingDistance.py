# -*-coding:utf-8-*-
def hammingDistance(x, y):
    n = x ^ y
    a = 0
    while n & 0xffffffff != 0:
        a += 1
        n = n & (n - 1)
    print(a)
    return a


hammingDistance(4, 1)
hammingDistance(5, 1)
hammingDistance(93, 73)


