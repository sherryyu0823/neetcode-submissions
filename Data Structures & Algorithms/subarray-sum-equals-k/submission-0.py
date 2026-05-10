class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur = 0
        ans = 0
        # range A - range B = k
        # range A - k = range B
        pre = {0:1}
        for n in nums:
            cur += n
            if cur - k in pre:
                ans+= pre[cur - k]
            if cur in pre:
                pre[cur]+=1
            else:
                pre[cur] = 1
        return ans
            
                
