# -*-coding:utf-8-*-
def removeDuplicates(nums):
    if nums == None: return 0
    a=0
    for i in range(1,len(nums)):
        if nums[a]!=nums[i]:
            a+=1
            nums[a]=nums[i]
    nums=nums[0:a+1]
    print(a+1)
    print(nums)



removeDuplicates([1,1,2,3,4,5,5,6])
removeDuplicates([1])
removeDuplicates([1,1])
removeDuplicates([1,2])
