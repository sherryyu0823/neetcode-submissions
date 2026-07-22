class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        ts, te = intervals[0]

        for i in range(1, len(intervals)):

            # overlap
            if te >= intervals[i][0]:
                te = max(te, intervals[i][1])
            else:
                ans.append([ts, te])
                ts, te = intervals[i][0], intervals[i][1]

        ans.append([ts, te])
        return ans


