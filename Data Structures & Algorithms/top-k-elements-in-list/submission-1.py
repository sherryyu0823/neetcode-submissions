class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        ans = []
        for n in nums:
            freq[n]+=1
        heap = []
        for n in freq.keys():
            heapq.heappush(heap, (-freq[n], n))
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
        