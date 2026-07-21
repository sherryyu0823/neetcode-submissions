class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l < r:
            cap = (l+r) // 2
            tmp = 0
            d = 1
            i = 0
            while i < len(weights):
                tmp += weights[i]
                if tmp <= cap: i += 1
                else:
                    d += 1
                    tmp = 0
                    # weights[i] = tmp-cap
            
            if d > days: l = cap + 1
            else: r = cap

        return l


                
