# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodCount = 0
        
        def dfs(root, maxVal):
            nonlocal goodCount

            if not root:
                return None
            
            if root.val >= maxVal:
                goodCount += 1
                maxVal = root.val
            
            dfs(root.left, maxVal)
            dfs(root.right, maxVal)
        
        dfs(root, -101)

        return goodCount
