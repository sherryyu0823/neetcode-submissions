class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        house0 = nums[:n-1]
        house1 = nums[1:n]

        r0 = [-1]*(n-1)
        r1 = [-1]*(n-1)

        r0[0] = house0[0]
        r1[0] = house1[0]
        r0[1] = max(house0[1], house0[0])
        r1[1] = max(house1[1], house1[0])

        for i in range(2,len(house0)):
            r0[i] = max(house0[i]+r0[i-2], r0[i-1])
        
        for i in range(2,len(house1)):
            r1[i] = max(house1[i]+r1[i-2], r1[i-1])
            
        return max(r1[-1], r0[-1])


