class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        
        for p in points:
            x = p[0]
            y = p[1]
            dist = x**2+y**2
            maxheap.append((-dist, p))
        
        heapq.heapify(maxheap)

        while k < len(maxheap):
            heapq.heappop(maxheap)
        ans = []
        for n in maxheap:
            ans.append(n[1])
        return ans
