#-*-coding:utf-8-*-
def mySqrt(x):
    if x<=2:
        print(1)
        return 1
    left=0
    right=x
    while left<right:
        mid=int((right+left)/2)
        sqrt=int(x/mid)
        if sqrt==mid :
            print(mid)
            return (mid)
        if sqrt+1 ==mid:
            print(mid-1)
            return mid-1
        if sqrt-1 ==mid:
            print(mid)
            return mid
        elif sqrt < mid -1:
            right = mid
        elif sqrt >mid+1:
            left = mid
    print(int(mid))
    return mid

mySqrt(1)
mySqrt(2)
mySqrt(3)
mySqrt(4)
mySqrt(9)
mySqrt(6)
mySqrt(10)
mySqrt(24)
