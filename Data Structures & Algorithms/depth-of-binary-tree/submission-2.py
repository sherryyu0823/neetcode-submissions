# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursion
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         def getheight(node):
#             if not node:
#                 return 0
#             else:
#                 return max(getheight(node.left), getheight(node.right)) + 1
#         return getheight(root)

# BFS
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if root:
#             queue = deque([root])
#         else:
#             return 0

#         level = 0
#         while queue:
#             for i in range(len(queue)):
#                 node = queue.popleft()
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             level += 1
#         return level

# DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            stack = [[root, 1]]
        else:
            return 0

        max_depth = 0
        while stack:
            node = stack.pop()
            child = node[0]
            level = node[1]
            if child:
                max_depth = max(max_depth, level)
                if child.left:
                    stack.append([child.left, level+1])
                if child.right:
                    stack.append([child.right, level+1])
        return max_depth