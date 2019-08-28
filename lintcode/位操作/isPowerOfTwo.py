#-*-coding:utf-8-*-
def isPowerOfTwo(n):
    if n<0:return False
    a=0
    while n & 0xffffffff !=0:
        a += 1
        n=n&(n-1)
    if a==1:
        print(True)
        return True
    else:
        print(False)
        return False

isPowerOfTwo(1)
isPowerOfTwo(4)
isPowerOfTwo(6)
isPowerOfTwo(16)
isPowerOfTwo(18)
isPowerOfTwo(-2147483648)