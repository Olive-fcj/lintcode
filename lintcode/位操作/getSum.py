#-*-coding:utf-8-*-
def getSum(a,b):
    if (a>0 and b>0) or (a<0 and b<0):
       print(mySum(a,b))
    if a<=0:
        print(mySum(b,findComplement(a)))
    if b<=0:
        print(mySum(a,findComplement(b)))


def mySum(a1,b1):
    carry=(a1&b1)<<1
    sum=a1^b1
    res=carry^sum
    return res
def findComplement(num):
    mask = num;
    mask |= mask >> 1
    mask |= mask >> 2
    mask |= mask >> 4
    mask |= mask >> 8
    mask |= mask >> 16
    return mask ^ num



getSum(1,2)
getSum(1,5)
getSum(-1,2)
getSum(-2,1)
getSum(-2,-3)
getSum(-5,1)
getSum(-4,-6)
getSum(0,1)
getSum(-4,0)