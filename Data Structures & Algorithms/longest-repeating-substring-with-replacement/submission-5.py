class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        maxl = 0
        max_freq = 0
        ans = 0
        cnt = defaultdict(int)
        for r in range(len(s)):
            cnt[s[r]]+=1
            length = r-l+1
            max_freq = max(max_freq, cnt[s[r]])
            
            if length-max_freq > k:
                cnt[s[l]] -= 1
                if l+1 < len(s): l += 1
            
            ans = max(ans, r-l+1)
        
        return ans
