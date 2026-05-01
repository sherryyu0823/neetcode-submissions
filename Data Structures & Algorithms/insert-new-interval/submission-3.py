class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        newlist = []
        i = 0
        flag = 0
        while i < len(intervals):
            if intervals[i][0] < newInterval[0]:
                newlist.append(intervals[i])
                i += 1
            elif intervals[i][0] >= newInterval[0] and flag == 1:
                newlist.append(intervals[i])
                i += 1
            else:
                newlist.append(newInterval)
                flag = 1
        
        if flag == 0:
            newlist.append(newInterval)

        ans = [newlist[0]]

        for i in newlist:
            start, end = i
            if start<=ans[-1][1]:
                ans[-1][1] = max(end, ans[-1][1])
            else:
                ans.append(i)
        
        return ans
