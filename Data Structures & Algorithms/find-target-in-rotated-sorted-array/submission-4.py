class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def BS(l, r):
            while l<=r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                if nums[mid]<target:
                    l = mid+1
                if nums[mid]>target:
                    r = mid-1
 
            return -1
        def findmin():
            l, r = 0, len(nums)-1
            while l < r:
                mid = (l+r)//2
                if nums[mid] < nums[r]:
                    r = mid
                else:
                    l = mid+1
            return l
        piviot = findmin()
        # left
        if BS(0, piviot-1) == -1:
            return BS(piviot, len(nums)-1)
        else:
            return BS(0, piviot-1)
                