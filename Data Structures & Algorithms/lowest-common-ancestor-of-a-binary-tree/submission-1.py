# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def DFS(node):

            if node == None: return None
            
            if node == p or node == q:
                return node
            
            left = DFS(node.left)
            right = DFS(node.right)

            if left and right: return node
            if left: return left
            else: return right

    
        return DFS(root)

