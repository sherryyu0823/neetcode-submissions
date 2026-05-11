class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        cnt = set()
        ans = 0
        for r in range(len(s)):
            while s[r] in cnt:
                cnt.remove(s[l])
                l += 1
            cnt.add(s[r])
        
            ans = max(ans, len(cnt))
        return ans
            

        