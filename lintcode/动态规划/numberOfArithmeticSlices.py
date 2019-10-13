#-*-coding:utf-8-*-
def numberOfArithmeticSlices(A):
    if len(A) < 3:return 0
    count = 0
    sum = 0
    for i in range(2,len(A)):
        if A[i] - A[i-1] ==A[i-1] - A[i-2]:
            count = count+1
            sum += count
        else:
            count = 0
    print(sum)


numberOfArithmeticSlices([1,2,3,4])
numberOfArithmeticSlices([7,7,7,7])
numberOfArithmeticSlices([1,2,3,4,5])
numberOfArithmeticSlices([1, 1, 2, 5, 7])
numberOfArithmeticSlices([1,2,3,8,9,10])
