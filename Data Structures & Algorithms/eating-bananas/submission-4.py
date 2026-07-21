class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = float('inf')
        while l < r:
            rate = (l+r)//2
            hour = 0
            for p in piles:
                hour += math.ceil(p/rate)
            if hour > h: l = rate + 1
            else:
                r = rate
                
        
        return l
