# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node, last):
            nonlocal ans
            if node.val>=last:
                ans += 1
            if not node.left and not node.right:
                return
            last = max(node.val, last)
            if node.left:
                dfs(node.left, last)
            if node.right:
                dfs(node.right, last)
        
        dfs(root, float('-inf'))

        return ans
            

