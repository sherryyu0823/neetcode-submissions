from functools import lru_cache
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        course = defaultdict(list)
        for pre, c in prerequisites:
            course[c].append(pre)
        ans = []
  
        # @lru_cache(None)  
        memo = {}   
        def DFS(pre, crs):
            if (pre, crs) in memo:
                return memo[(pre, crs)]
            for c in course[crs]:
                if c == pre:
                    memo[(pre, c)] = True
                    return True
                if DFS(pre, c):
                    memo[(pre, c)] = True
                    return True
            memo[(pre, crs)] = False
            return False

        for pre, c in queries:
            ans.append(DFS(pre, c))
        
        return ans



