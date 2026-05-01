class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        j = 0
        ans = []
        l = 0
        while j < len(queries):
            length = []
            for u in intervals:
                s, e = u
                if s <= queries[j] <= e:
                    length.append(e-s+1)
            
            j += 1
            heapq.heapify(length)
            if len(length) == 0:
                ans.append(-1) 
            else:
                ans.append(heapq.heappop(length))
        return ans