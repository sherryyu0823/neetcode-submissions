class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dist = []
        for x, y in points:
            d = x**2 + y**2
            heapq.heappush(dist, (d, x, y))
        ans = []
        for _ in range(k):
            d, x, y = heapq.heappop(dist)
            ans.append([x, y])

        return ans
