#-*-coding:utf-8-*-
def rob (nums):
    if not nums: return 0
    if len(nums) == 1: return nums[0]

    def helper(nums):
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        return dp[-1]

    print(max(helper(nums[1:]), helper(nums[:-1])))




rob([2,3,2])
rob([1,2,3,4])
rob([3,2,3,1,2])
rob([1,4,3,1,3,4])
rob([2,1,1,2])