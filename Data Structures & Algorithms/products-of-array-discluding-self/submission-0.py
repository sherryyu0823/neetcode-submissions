class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tmp = 1
        ans = []
        zero = []
        for i in range(len(nums)):
            n = nums[i]
            if n != 0:
                tmp*=n
            else:
                tmp *= 1
                zero.append(i)

        if len(zero) == 0:
            for n in nums:
                ans.append(tmp//n)
        elif len(zero) == 1:
            ans = [0]*len(nums)
            ans[zero[0]] = tmp

        else:
            ans = [0]*len(nums)

        return ans
            
         
