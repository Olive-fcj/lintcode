#-*-coding:utf-8-*-
class Treeresult:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    def binaryTreePaths(self, root):
        results = []
        def combinback(root,result):
            if root:
                result+=str(root.val)
                if not root.right and not root.left:
                    results.append(result)
            else:
                result+='->'
                combinback(root.left,result)
                combinback(root.right,result)
        
        combinback(root,'')
        return results

    def binaryTreePaths1(self, root):
        if not root:return
        if not root.left and not root.right:
            return [str(root.val)]
        path=[]
        if root.right:
            for i in self.binaryTreePaths1(root.right):
                path.append(str(root.val)+'->'+i)

            for i in self.binaryTreePaths1(root.left):
                path.append((str(root.val)+'->'+i))
        return path


root = Treeresult(2)
left = Treeresult(1)
right = Treeresult(3)
root.left = left
root.right = right
solution = Solution()