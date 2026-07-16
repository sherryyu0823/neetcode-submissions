class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        cur = 0
        num = set(nums)

        for n in num:
            if n-1 not in num: # find starting point
                cur = 1
                while n+cur in num:
                    cur += 1
            ans = max(ans, cur)
        
        return ans

            
