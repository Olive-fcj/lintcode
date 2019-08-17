# -*-coding:utf-8-*-
def singleNumbers(A):
    if len(A) == 0: return
    l, r = 0, len(A) - 1
    A = sorted(A)
    while l < r:
        mid = int((l + r) / 2)
        if mid == 0:
            return A[0]
        if mid == len(A) - 1:
            return A[mid]
        if A[mid] != A[mid - 1] and A[mid] != A[mid + 1]:
            return A[mid]
        if (A[mid] == A[mid - 1] and mid % 2 == 0) or (A[mid] == A[mid + 1] and (mid + 1) % 2 == 0):
            r = mid - 1
        if (A[mid] == A[mid - 1] and mid % 2 != 0) or (A[mid] == A[mid + 1] and (mid + 1) % 2 != 0):
            l = mid + 1

    if r == 0:
        return A[0]
    if r == len(A) - 1:
        return A[len(A) - 1]
    if A[r] != A[r - 1] and A[r] != A[r + 1]:
        return A[r]
    if A[r - 1] != A[r - 2] and A[r] != A[r - 1]:
        return A[l]


print(singleNumbers([1, 1, 2, 2, 4, 4, 5, 6, 7, 6, 7, 100, -1, -2, -1, 100, 3, -2, 3]))
