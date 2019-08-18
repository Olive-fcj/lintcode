#-*-coding:utf-8-*-
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def inorderTraversal(self, root):
        # write your code here
        stack = []
        sol = []
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                sol.append(curr.val)
                curr = curr.right
        print(sol)

    def insertNode(self,root,node):
        if root==None:return node
        curr=root
        while True:
            if node.val < curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = node
                    return root
            else:
                if curr.right:
                    curr=curr.right
                else:
                    curr.right=node
                    return root

    # def myInsertNode(self,root,node):
    #     if root ==None:return node
    #     curr=root
    #     while True:
    #         if node.val > curr.val:
    #             if curr.right:
    #                 curr=curr.right
    #             else:
    #                 curr.right=node
    #                 return root
    #         else:
    #             if curr.left:
    #                 curr=curr.left
    #             else:
    #                 curr.left=node
    #                 return root


solution = Solution()
tree = solution.insertNode(None,TreeNode(8))
solution.insertNode(tree,TreeNode(5))
solution.insertNode(tree,TreeNode(12))
solution.insertNode(tree,TreeNode(3))
solution.insertNode(tree,TreeNode(6))
solution.insertNode(tree,TreeNode(9))
solution.insertNode(tree,TreeNode(14))
solution.inorderTraversal(tree)

# tree = solution.myInsertNode(None,TreeNode(8))
# solution.myInsertNode(tree,TreeNode(5))
# solution.myInsertNode(tree,TreeNode(12))
# solution.myInsertNode(tree,TreeNode(3))
# solution.myInsertNode(tree,TreeNode(6))
# solution.myInsertNode(tree,TreeNode(9))
# solution.myInsertNode(tree,TreeNode(14))
# solution.inorderTraversal(tree)




