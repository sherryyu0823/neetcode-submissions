from functools import lru_cache
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        course = defaultdict(list)
        for pre, c in prerequisites:
            course[c].append(pre)
        ans = []

        path = set()
        visit = set()   
        @lru_cache(None)     
        def DFS(pre, crs):
            # if pre in visit:
            #     return True
            for c in course[crs]:
                if c == pre:
                    return True
                if DFS(pre, c):
                    return True

            return False

        for pre, c in queries:
            ans.append(DFS(pre, c))
        
        return ans



