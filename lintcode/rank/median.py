#-*-coding:utf-8-*-
def median(nums):
    nums=sorted(nums)
    a=len(nums)/2
    if len(nums)%2==0:
        print(nums[int(a)-1])
    else:
        print(nums[int(a)])

median([4,5,1,2])