# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        preOrder = []
        def dfs(node):
            
            if not node:
                return None
            
            dfs(node.left)
            preOrder.append(node.val)
            if len(preOrder) == k:
                return
            dfs(node.right)

        dfs(root)
        print(preOrder)
        return preOrder[k - 1]


            
