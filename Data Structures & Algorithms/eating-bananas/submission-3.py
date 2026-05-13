class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # rate = math.inf()

        if h == len(piles):
            return max(piles)

        l, r = 1, max(piles)

        while l<=r:
            mid = (l+r)//2
            hours = 0

            for p in piles:
                if mid>=p:
                    hours+=1
                if mid < p:
                    hours += math.ceil(p/mid)
            
            if hours > h:
               l = mid+1
            else:
                r = mid-1

        return l 