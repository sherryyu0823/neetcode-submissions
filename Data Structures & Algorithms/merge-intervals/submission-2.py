class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        tmp = -1
        ans = [intervals[0]]
        last_end = ans[0][1]
        for i in intervals[1:]:
            start, end = i
            if start <= ans[-1][1]:
                ans[-1][1] = max(end, ans[-1][1])
            else:
                ans.append(i)
            
        return ans