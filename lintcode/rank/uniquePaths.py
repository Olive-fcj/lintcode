# -*-coding:utf-8-*-
def uniquePaths(m, n):
    if m == 0 or n == 0: return None
    if m == 1 or n == 1:
        print(1)
        return 1
    if m == 2 and n == 2:
        print(2)
        return 2
    if m >= 3 or n >= 3:
        list = [[1] * m for _ in range(n)]
        for i in range(1, m):
            for j in range(1, n):
                list[j][i] = list[j][i - 1] + list[j - 1][i]
        print(list[n - 1][m - 1])


uniquePaths(3, 3)
uniquePaths(2, 2)
uniquePaths(1, 3)
uniquePaths(3, 4)
uniquePaths(4, 3)
uniquePaths(2, 4)
