class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        def isPal(l, r, s):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        while l<r:
            if s[l]!=s[r]:
                return isPal(l+1, r, s) or isPal(l, r-1, s)
            l+=1
            r-=1
        return True
        