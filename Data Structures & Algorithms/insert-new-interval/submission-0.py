class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x:x[0])

        ans = [intervals[0]]

        for i in intervals:
            start, end = i
            if start<=ans[-1][1]:
                ans[-1][1] = max(end, ans[-1][1])
            else:
                ans.append(i)
        
        return ans