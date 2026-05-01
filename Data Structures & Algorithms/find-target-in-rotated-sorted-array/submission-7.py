class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid+1
        piviot = l

        def BS(l, r):
            while l<=r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid+1
                else:
                    r = mid-1

            return -1


        
        if BS(0, piviot-1) != -1:
            return BS(0, piviot-1)
        else:
            return BS(piviot, len(nums)-1)
