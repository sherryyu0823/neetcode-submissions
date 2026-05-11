class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        cnt = defaultdict(int)
        for n in nums:
            cnt[n] +=1
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                s = nums[l]+nums[r]+nums[i]

                if s == 0:
                    ans.append([nums[l], nums[r], nums[i]])
                    # skip the repetitive
                    while l<r and nums[l] == nums[l+1]: l+=1
                    while l<r and nums[r] == nums[r-1]: r-=1
                    l+=1
                    r-=1
                if s < 0:
                    l+=1
                if s > 0:
                    r-=1
            
        
        return ans
