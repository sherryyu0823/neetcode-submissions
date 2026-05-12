class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')', '{':'}', '[':']'}
        stack = []
        for c in s:
            if c in dic:
                stack.append(c)
            else:
                if not stack:
                    return False
                l = stack.pop()
                if c==dic[l]:
                    pass
                else:
                    return False
        return not stack

            

