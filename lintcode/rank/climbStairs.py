# -*-coding:utf-8-*-
def climbStairs(n):
    # write your code here
    if n == 1: return 1
    if n == 2: return 2
    if n == 3: return 3
    if n > 3:
        list = n * [1]
        list[1] = 2
        list[2] = 3
        for i in range(3, n):
            list[i] = (list[i - 1] + list[i - 2])
    print(list[n - 1])


climbStairs(7)
climbStairs(6)
climbStairs(5)
climbStairs(4)
climbStairs(3)
climbStairs(2)
climbStairs(1)
