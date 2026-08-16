class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1
        
        heap = []
        for key, v in freq.items():
            heapq.heappush(heap, (-v, key))
        
        ans = []

        for _ in range(k):
            v, key = heapq.heappop(heap)
            ans.append(key)
        
        return ans