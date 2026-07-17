class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        i = 0
        for i in range(len(temperatures)):
            j = i
            while j < len(temperatures):
                if temperatures[j]>temperatures[i]:
                    ans.append(j-i)
                    break
                j += 1
            if j == len(temperatures):
                ans.append(0)
        return ans