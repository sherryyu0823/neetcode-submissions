class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        for p in prerequisites:
            a, b = p
            adj[b].append(a)

        visited = {i:0 for i in range(numCourses)}

        def dfs(crs):
            if visited[crs] == 1:
                return False   # cycle
            if visited[crs] == 2:   # finished
                return True
            visited[crs] = 1    #visiting

            for c in adj[crs]:
                if not dfs(c):
                    return False
            visited[crs] = 2    # finished
            
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
