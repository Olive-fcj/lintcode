#-*-coding:utf-8-*-

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        stack=[]
        sol=[]
        curr=root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr=curr.left
            else:
                curr=stack.pop()
                sol.append(curr.val)
                curr=curr.right
        print(sol)

root = TreeNode(2)
left = TreeNode(1)
right = TreeNode(3)
root.left = left
root.right = right
solution = Solution()
solution.inorderTraversal(root)



