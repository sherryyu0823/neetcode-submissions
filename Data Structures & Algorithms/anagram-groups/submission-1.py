class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        # for s in strs:
        #     key = tuple(sorted(s))
        #     group[key].append(s)
        # Optimized O(m*n)
        for s in strs:
            cnt = [0]*26
            for c in s:
                cnt[ord(c)-ord('a')] += 1
            key = tuple(cnt)
            group[key].append(s)
        return(list(group.values()))

