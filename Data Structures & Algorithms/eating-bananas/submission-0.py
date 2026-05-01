class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def eat(rate):
            cur_p = 0
            cur_h = 0
            for p in piles:
                cur_h += math.ceil(p / rate)
            if cur_h> h:
                return False
            else:
                return True
        
        l, r = 1, max(piles)

        while l<=r:
            mid = (l+r)//2
            if eat(mid):
                r = mid-1
            else:
                l = mid+1
        
        return l