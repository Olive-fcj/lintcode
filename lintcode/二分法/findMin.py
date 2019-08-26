#-*-coding:utf-8-*-
def findMin(nums):
    if len(nums)==1:return nums[0]
    if nums[0] < nums[1] and nums[0] < nums[len(nums)-1]:
        print(nums[0])
        return nums[0]
    if nums[len(nums)-1] <nums[0] and nums[len(nums)-1]<nums[len(nums)-2]:
        print(nums[len(nums)-1])
        return nums[len(nums)-1]
    left=0
    right=len(nums)-1
    while left<right:
        mid = int((left+right)/2)
        if nums[mid]<nums[mid-1] and nums[mid] <nums[mid+1]:
            print(nums[mid])
            return nums[mid]
        elif nums[mid] > nums[mid-1] and nums[mid] >nums[mid+1]:
            print(nums[mid+1])
            return nums[mid+1]
        elif nums[mid] > nums[0]:
            left=mid
        elif nums[mid] < nums[0]:
            right=mid
    print(nums[mid])
    return nums[mid]

findMin([1,2,3,4,5])
findMin([2,3,4,5,1])
findMin([4,5,1,2,3])
findMin([4,5,6,0,1,2,3])
findMin([4,5,7,1,2,3])
