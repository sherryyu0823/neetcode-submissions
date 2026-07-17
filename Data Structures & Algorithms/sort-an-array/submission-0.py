class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ans = []

        heapq.heapify(nums)

        while nums:
            ans.append(heapq.heappop(nums))
        return ans