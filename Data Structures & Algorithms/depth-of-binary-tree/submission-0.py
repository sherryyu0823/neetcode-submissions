# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def getheight(node):
            if not node:
                return 0
            else:
                return max(getheight(node.left), getheight(node.right)) + 1
        return getheight(root)