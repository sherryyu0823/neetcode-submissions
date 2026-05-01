class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        
        for p in points:
            x = p[0]
            y = p[1]
            dist = x**2+y**2
            # maxheap.append((-dist, p))

            # optimized
            heapq.heappush(maxheap, (-dist, p))
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        
        # heapq.heapify(maxheap)

        ans = []
        for n in maxheap:
            ans.append(n[1])
        return ans
