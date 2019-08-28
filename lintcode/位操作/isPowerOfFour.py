#-*-coding:utf-8-*-
def isPowerOfFour(num):
    if num<0:return False
    a = 0
    if num&0b01010101010101010101010101010101 !=0:
        while num & 0xffffffff !=0:
            a+=1
            num=num & (num-1)
    if a==1:
        print(True)
        return True
    else:
        print(False)
        return False

isPowerOfFour(1)
isPowerOfFour(16)
isPowerOfFour(18)
isPowerOfFour(32)
isPowerOfFour(64)
isPowerOfFour(128)
isPowerOfFour(65536)