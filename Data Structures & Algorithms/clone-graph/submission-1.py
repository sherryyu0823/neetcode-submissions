"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            return None
        q = deque()
        visited = {}
        copy = Node(node.val)
        def find(node):
            q.append(node)
            visited[node] = Node(node.val)
            while q:
                old = q.popleft()
                for n in old.neighbors:
                    if n not in visited:
                        q.append(n)
                        visited[n] = Node(n.val)

                    visited[old].neighbors.append(visited[n])
            
            return visited[node]


        return find(node)