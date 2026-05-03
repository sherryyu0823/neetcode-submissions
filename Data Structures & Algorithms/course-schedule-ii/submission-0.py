class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course = defaultdict(list)
        for c, pre in prerequisites:
            course[c].append(pre)

        path = set()
        visit = set()
        ans = []
        def DFS(crs):
            if crs in path:
                return False
            if crs in visit:
                return True
            
            path.add(crs)
            for c in course[crs]:
                if not DFS(c):
                    return False
            
            path.remove(crs)
            ans.append(crs)
            visit.add(crs)
            return True

        for c in range(numCourses):
            if not DFS(c):
                    return []
        return ans
