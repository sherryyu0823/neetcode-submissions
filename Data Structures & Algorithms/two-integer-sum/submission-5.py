class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num = []
        for i in range(len(nums)):
            num.append((nums[i], i))

        num.sort()
        l, r = 0, len(nums)-1

        while l<r:
            if num[l][0] + num[r][0] == target:

                return [min(num[l][1], num[r][1]), max(num[l][1], num[r][1])]
            if num[l][0] + num[r][0] > target:
                r-=1
            if num[l][0] + num[r][0] < target:
                l+=1
        
        return []
            
            