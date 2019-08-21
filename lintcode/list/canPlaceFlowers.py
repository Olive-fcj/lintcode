#-*-coding:utf-8-*-
def canPlaceFlowers(flowerbed,n):
    a=0
    if flowerbed==None:
        print(False)
        return False
    if len(flowerbed)==1 and flowerbed[0]==0:
        print(True)
        return True
    if len(flowerbed)==2:
        if (flowerbed[0]==0 and flowerbed[1]==0) and n==1:
            print(True)
            return True
    if flowerbed[0]==0 and flowerbed[1]==0:
        flowerbed[0]=1
        a+=1

    if flowerbed[len(flowerbed)-1]==0 and flowerbed[len(flowerbed)-2]==0:
        flowerbed[len(flowerbed)-1]=1
        a+=1
    for i in range (1,len(flowerbed)-1):
        if flowerbed[i-1]==0 and flowerbed[i+1]==0:
            if flowerbed[i]==0:
                flowerbed[i]=1
                a+=1

    if a >=n:
        print(True)
        return True
    else:
        print(False)
        return False

canPlaceFlowers([1,0,0,0,1],1)
canPlaceFlowers([1,0,0,0,1],2)
canPlaceFlowers([1,1],1)
canPlaceFlowers([0,0],1)
canPlaceFlowers([0,0,1,0,1],1)
canPlaceFlowers([0,0,1,0,0],2)
