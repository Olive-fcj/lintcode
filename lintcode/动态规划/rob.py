#-*-coding:utf-8-*-
def rob(num):
    if len(num) ==1:
        return num[0]
    if len(num) ==2:
        return max(num[0],num[1])
    else:
        num[1] = max(num[0],num[1])
        for i in range(2,len(num)):
            num[i] = max(num[i-1],num[i-2]+num[i])
    print(num[len(num)-1])
rob([2,1,1,2])