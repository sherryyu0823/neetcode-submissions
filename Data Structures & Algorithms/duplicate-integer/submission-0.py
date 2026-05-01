class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = set()
        for i in range(0, len(nums)):
            if nums[i] in d:
                return True
            else:
                d.add(nums[i])
        return False