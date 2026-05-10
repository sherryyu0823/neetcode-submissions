class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i in range(len(nums)):
            A.append((nums[i], i))
        
        A.sort()

        l, r = 0, len(A)-1
        cur = 0
        cur = 0
        while l<r:
            v1, i1 = A[l]
            v2, i2 = A[r]

            cur  = v1+v2
            if cur == target:
                return [min(i1, i2), max(i1, i2)]
            if cur > target:
                r -= 1
            if cur < target:
                l += 1
        
        return [] 