class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)
        heap = []
        for n in nums:
            cnt[n] += 1
        for key in cnt.keys():
            heapq.heappush(heap, (-cnt[key], key))
        ans = []
        
        for _ in range(k):
            v, key = heapq.heappop(heap)
            ans.append(key)
        
        return ans