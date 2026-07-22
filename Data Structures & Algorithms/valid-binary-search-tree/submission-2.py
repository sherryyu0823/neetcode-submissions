# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def DFS(node, minv, maxv):
            
            if not node: return True

            if not (minv < node.val < maxv): return False
            else: return DFS(node.right, node.val, maxv) and \
            DFS(node.left, minv, node.val)
            
        
        

        return DFS(root, float('-inf'), float('inf'))

