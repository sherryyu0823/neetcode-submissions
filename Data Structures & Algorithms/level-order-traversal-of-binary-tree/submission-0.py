# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque([root])
        order = []
        order.append([root.val])
        while q:
            level = []
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if node.left:
                    level.append(node.left.val)
                    q.append(node.left)
                if node.right:
                    level.append(node.right.val)
                    q.append(node.right)

            order.append(level)
        
        order.pop()
        return order