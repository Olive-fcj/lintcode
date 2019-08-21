#-*-coding:utf-8-*-
def subarraySum(nums):
    a = 0
    b=0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            a += nums[j]
            if a == 0:
                b+=1
                print([i,j])
                return [i, j]
    if b==0:
        print('The sum of the subarray you return is 0.')


subarraySum([-3,1,2,-3,4])
subarraySum([1,0,1])