class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        check = defaultdict(int)
        for i in nums:
            check[i] += 1
        for k, v in check.items():
            if v == 1:
                return k