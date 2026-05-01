# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         def getheight(node):
#             if not node:
#                 return 0
#             else:
#                 return max(getheight(node.left), getheight(node.right)) + 1
#         return getheight(root)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            queue = deque([root])
        else:
            return 0
        level = 0
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return level