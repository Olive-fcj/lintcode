# -*-coding:utf-8-*-
def minPathSum(grid):
    if grid == None: return
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                grid[0][j] = grid[0][j - 1] + grid[0][j]
            elif j == 0:
                grid[i][0] = grid[i - 1][0] + grid[i][0]
            elif len(grid) >= 2 and len(grid[0]) >= 2:
                grid[i][j] = min(grid[i - 1][j] + grid[i][j], grid[i][j - 1] + grid[i][j])
    print(grid[len(grid) - 1][len(grid[0]) - 1])


def minPathSum1(grid):
    if grid is None: return
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                grid[0][j] = grid[0][j - 1] + grid[0][j]
            elif j == 0:
                grid[i][0] = grid[i - 1][0] + grid[i][0]
            # elif len(grid) >= 2 and len(grid[0]) >= 2:
            else:
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
    print(grid[len(grid) - 1][len(grid[0]) - 1])


minPathSum([[1, 2, 3, 4]])
minPathSum([[1], [2], [3], [4]])
minPathSum([[1, 2], [3, 4]])
minPathSum([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
])
