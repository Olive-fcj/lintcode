#-*-coding:utf-8-*-
def diffWaysToCompute(input):
    if input.isdigit():
        return [int(input)]
    print(input)
    res=[]
    for i in range(len(input)):
        if input[i] in "+-*":
            res1=diffWaysToCompute(input[:i])
            res2=diffWaysToCompute(input[i+1:])
            for j in res1:
                for k in res2:
                    res.append(operator(j,k,input[i]))
    return sorted(res)
def operator(m,n,op):
    if op=='+':
        return m+n
    if op=="-":
        return m-n
    else:
        return m*n

print(diffWaysToCompute("2-1-1"))
print(diffWaysToCompute("2*3-4*5"))