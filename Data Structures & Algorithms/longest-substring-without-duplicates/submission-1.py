class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seq = {}
        l = 0
        ans = 0
        for r in range(len(s)):
            while s[r] in seq and l<r:
                seq.pop(s[l])
                l += 1
            seq[s[r]] = 1
            ans = max(r-l+1, ans)

        return ans