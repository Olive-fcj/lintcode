#-*-coding:utf-8-*-
def reverseBits(n):
    a=32
    res=0
    while a:
        res<<=1
        res+=n&1
        n>>=1
        a-=1
    print(int(bin(res),2))

reverseBits(110110110110110110110110)
reverseBits(110110110110110111111111)
reverseBits(111011011011011011011011)
reverseBits(101011011011011011011000)
