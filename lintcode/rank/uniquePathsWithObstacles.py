#-*-coding:utf-8-*-
def uniquePathsWithObstacles(obstacleGrid):
    list= [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
    for i in range (len(obstacleGrid)):
        for j in range (len(obstacleGrid[0])):
            if i==0 and j==0:
                    if obstacleGrid[0][0]==0:
                        list[0][0]=1
                    else:
                        print(0)
                        return 0
            elif i == 0 :
                if obstacleGrid[0][j]==0:
                    list[0][j]=list[0][j-1]
            elif j == 0:
                if obstacleGrid[i][0] == 0:
                    list[i][0]=list[i-1][0]
            elif i>0 and j>0:
                if obstacleGrid[i][j]==0:
                    list[i][j]=list[i-1][j]+list[i][j-1]
                else:
                    list[i][j]=0
    print(list[len(list) - 1][len(list[0])-1])
    return list[len(list)-1][len(list[0])-1]


uniquePathsWithObstacles([[0]])
uniquePathsWithObstacles([[1]])
uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
uniquePathsWithObstacles([[1,0,0],[0,1,0],[0,0,0]])
uniquePathsWithObstacles([[0,1,0],[0,1,0],[0,0,0]])
uniquePathsWithObstacles([[0,0],[0,0],[0,0],[1,0],[0,0]])
