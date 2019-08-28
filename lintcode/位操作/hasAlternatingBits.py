#-*-coding:utf-8-*-
def hasAlternatingBits(n):
    if n <0 :return False
    a=n^(n>>1)
    print(a&(a+1)==0)
    return a&(a+1)==0

hasAlternatingBits(5)
hasAlternatingBits(1)
hasAlternatingBits(7)
hasAlternatingBits(10)
hasAlternatingBits(11)
hasAlternatingBits(4)