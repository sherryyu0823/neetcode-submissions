class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x:x[0])
        sq = []
        for i in range(len(queries)):
            sq.append((queries[i], i))
        sq = sorted(sq)

        ans = [-1] * len(queries)
        minheap = []
        i = 0
        for q in sq:
            while i < len(intervals) and intervals[i][0] <= q[0]:
                l, r = intervals[i][0], intervals[i][1]
                heapq.heappush(minheap, (r-l+1, r))
                i += 1
            
            while minheap and minheap[0][1] < q[0]:
                    heapq.heappop(minheap)
            if minheap:
        
                ans[q[1]] = minheap[0][0]
        
        return ans


