#-*-coding:utf-8-*-
def nextGreatestLetter(letters, target):
    left=0
    right=len(letters)-1
    if target<letters[0] or target > letters[right]:
        print(letters[0])
        return letters[0]
    if target == letters[right]:
        print(letters[right])
        return letters[right]
    if target==letters[0] and target !=letters[1]:
        print(letters[1])
        return letters[1]
    while left < right:
        mid = int((left+right)/2)
        if target >= letters[mid] and target < letters[mid+1]:
            print(letters[mid+1])
            return  letters[mid+1]
        elif target > letters[mid-1] and target < letters[mid]:
            print(letters[mid])
            return letters[mid]
        elif target >= letters[mid+1]:
            left = mid
        elif target <= letters[mid-1]:
            right = mid
    print(letters[mid])
    return letters[mid]

nextGreatestLetter(["c", "f", "j"],'a')
nextGreatestLetter(['a', 'b'],'z')
nextGreatestLetter(["c", "f", "j"],'c')
nextGreatestLetter(["c", "f", "j"],'j')
nextGreatestLetter(["c", "f", "j"],'k')
nextGreatestLetter(["c", "f", "j"],'e')
nextGreatestLetter(["e","e","e","e","e","e","n","n","n","n"],'e')






