class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        l, r = 1, max(piles)
        def eat(rate):
            t = 0
            for p in piles:
                t+=math.ceil(p/rate)
            if t>h:
                return False
            else:
                return True

        while l < r:
            mid = (l+r)//2
            if eat(mid):
                r = mid
            else:
                l = mid+1
        return l