#-*-coding:utf-8-*-
def printZMatrix(matrix):
    if matrix==None:return
    result=[]
    m=len(matrix)
    n=len(matrix[0])
    if  m==1:
        print(matrix[0])
        return matrix[0]
    list=[[] for i in range (m+n-1)]
    for i in range (m):
        for j in range(len(matrix[i])):
            list[i+j].append(matrix[i][j])

    for l in range (len(list)):
        if l%2==0:
            list[l].reverse()
        for k in range(len(list[l])):
            result.append(list[l][k])
    print(result)
    return result
printZMatrix([[1,2,3],[4,5,6],[7,8,9]])
printZMatrix([[1,2,3,4]])
printZMatrix([[1],[2],[3],[4]])
printZMatrix([[1,2],[3,4]])





