#-*-coding:utf-8-*-
def findComplement(num):
    mask = num;
    mask |= mask >> 1;
    mask |= mask >> 2;
    mask |= mask >> 4;
    mask |= mask >> 8;
    mask |= mask >> 16;
    print (mask ^ num);

findComplement(5)
findComplement(1)
findComplement(6)
findComplement(8)