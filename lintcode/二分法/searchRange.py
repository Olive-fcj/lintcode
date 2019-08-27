# -*-coding:utf-8-*-
class Solunstion:
    def searchRange(self,nums, target):
        if nums==[] or target not in nums:
            print([-1,-1])
            return [-1,-1]
        first = self.find(nums,target)
        second = self.find(nums,target+1)-1
        print([first,max(first,second)])
        return [first,max(first,second)]

    def find(self,nums,target):
        left = 0
        right = len(nums)
        while left < right:
            mid = int((left + right-1) / 2)
            if nums[mid] >= target:
                right=mid
            else:
                left=mid+1
        return left

a=Solunstion()
a.searchRange([2, 2], 2)
a.searchRange([1, 2, 3, 4, 5, 5, 6, 7], 5)
a.searchRange([1, 2, 2], 5)
a.searchRange([1, 2, 2], 2)
a.searchRange([1, 2, 2,3,4,5,6,], 1)
a.searchRange([1, 2, 2,3,4,5,6,], 6)
a.searchRange([1, 2, 2,3,4,6,6,], 6)
a.searchRange([1, 2], 2)
a.searchRange([1, 1], 1)
a.searchRange([1, 2], 1)
