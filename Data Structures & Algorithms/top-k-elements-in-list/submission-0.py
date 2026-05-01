class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)
        freq = [[] for _ in range(len(nums)+1)]
        for n in nums:
            cnt[n] += 1
        
        for num, fr in cnt.items():
            freq[fr].append(num)

        rev = []
        for i in range(len(freq)-1, 0, -1):
            if freq[i]:
                for n in freq[i]:
                    rev.append(n)
                if len(rev) == k:
                    return rev
