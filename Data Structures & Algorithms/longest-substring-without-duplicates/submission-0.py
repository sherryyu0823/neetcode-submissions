class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        l, r = 0, 0
        ans = 0
        for i in range(len(s)):
            while s[i] in st:
                st.remove(s[l])
                l+=1
            st.add(s[i])
            r = i
            ans = max(ans, r-l+1)
        return ans