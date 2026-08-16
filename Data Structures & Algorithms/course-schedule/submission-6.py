class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        q = deque()
        path = set()
        visited = set()
        def DFS(course):
            if course in path: return False
            if course in visited: return True

            path.add(course)
            for c in graph[course]:
                if not DFS(c): return False
            path.remove(course)
            visited.add(course)
            return True
        
        for i in range(numCourses):
            if not DFS(i): return False
        
        return True
