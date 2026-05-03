class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course = defaultdict(list)
        for c, pre in prerequisites:
            course[c].append(pre)

        path = set()
        visit = set()
        def DFS(crs):
            if crs in path:
                return False
            if crs in visit:
                return True
            path.add(crs)
            for val in course[crs]:
                if not DFS(val):
                    return False

            path.remove(crs)
            visit.add(crs)
            return True

        for crs in range(numCourses):
            if not DFS(crs):
                return False
        return True