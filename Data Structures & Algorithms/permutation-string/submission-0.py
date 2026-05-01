class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = [0]*26
        w = [0]*26
        n = len(s1)
        l = 0
        for c in s1:
            cnt[ord(c)-ord("a")]+=1
        for r in range(len(s2)):
            if r-l+1<n:
                w[ord(s2[r])-ord("a")] +=1
            if r-l+1 == n:
                w[ord(s2[r])-ord("a")] +=1
                if w==cnt:
                    return True
            if r-l+1 > n:
                w[ord(s2[l])-ord("a")]-=1
                w[ord(s2[r])-ord("a")]+=1
                l+=1
                if w == cnt: return True
        return False
