# -*-coding:utf-8-*-
def removeDuplicates(nums):
    if len(nums) == 1: return 1
    if nums == []:
        return []
    else:
        a = 0
        if nums[0] == nums[1]:
            a += 1
            nums[0] = nums[1]
        for i in range(0, len(nums) - 1):
            if (nums[a] != nums[i] and nums[i] == nums[i + 1]):
                a += 2
                nums[a], nums[a - 1] = nums[i], nums[i]
            if nums[a] != nums[i]:
                a += 1
                nums[a] = nums[i]
        if nums[a] != nums[len(nums) - 1]:
            a += 1
            nums[a] = nums[len(nums) - 1]
        nums = nums[0:a + 1]
        print(a + 1, nums)


def myremove(nums):
    if nums == None: return
    A = []
    for i in nums:
        if nums.count(i) == 1:
            A.append(i)
        elif i not in A and nums.count(i) >= 2:
            A.append(i)
            A.append(i)
    print(len(A), A)

def myremove1(nums):
    if nums==[]:return None
    if len(nums)==1:
        return  len(nums),nums
        print(len(nums),nums)
    if nums[0]==nums[1] and len(nums)==2:
        print(len(nums),nums)
        return len(nums), nums
    A=[]
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            A.append(nums[i])
        elif nums[i] ==nums[i+1] and nums[i] not in A:
            A.append(nums[i])
    if nums[len(nums)-1] not in A:
        A.append(nums[len(nums)-1])
    print(len(A),A)


myremove([1, 1, 2, 3, 4, 5, 5, 6])
myremove([1])
myremove([1, 1])
myremove([1, 2])
myremove([])
myremove(
    [-14, -14, -14, -14, -14, -14, -14, -13, -13, -13, -13, -12, -11, -11, -11, -9, -9, -9, -7, -7, -7, -6, -6, -5, -5,
     -5, -4, -4, -4, -3, -3, -3, -2, -2, -2, -1, -1, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6,
     6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10, 11, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 15, 16, 17,
     18, 18, 18, 20, 20, 21, 21, 21, 21, 21, 22, 22, 22, 22, 23, 24, 24, 25])
myremove1([1, 1, 2, 3, 4, 5, 5, 6])
myremove1([1])
myremove1([1, 1])
myremove1([1, 2])
myremove1([])
myremove1(
    [-14, -14, -14, -14, -14, -14, -14, -13, -13, -13, -13, -12, -11, -11, -11, -9, -9, -9, -7, -7, -7, -6, -6, -5, -5,
     -5, -4, -4, -4, -3, -3, -3, -2, -2, -2, -1, -1, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6,
     6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10, 11, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 15, 16, 17,
     18, 18, 18, 20, 20, 21, 21, 21, 21, 21, 22, 22, 22, 22, 23, 24, 24, 25])

removeDuplicates([1, 1, 2, 3, 4, 5, 5, 6])
removeDuplicates([1, 1, 2, 3, 4, 5, 5, 6, 6])
removeDuplicates([1])
removeDuplicates([1, 1])
removeDuplicates([1, 2])
removeDuplicates([])
removeDuplicates(
    [-14, -14, -14, -14, -14, -14, -14, -13, -13, -13, -13, -12, -11, -11, -11, -9, -9, -9, -7, -7, -7, -6, -6, -5, -5,
     -5, -4, -4, -4, -3, -3, -3, -2, -2, -2, -1, -1, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6,
     6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10, 11, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 15, 16, 17,
     18, 18, 18, 20, 20, 21, 21, 21, 21, 21, 22, 22, 22, 22, 23, 24, 24, 25])
