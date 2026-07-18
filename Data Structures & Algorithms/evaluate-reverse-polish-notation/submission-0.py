class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in "+-*/":
                if t == "+":
                    b = int(stack.pop())
                    a = int(stack.pop())
                    stack.append(a+b)
                elif t == "-":
                    b = int(stack.pop())
                    a = int(stack.pop())
                    stack.append(a-b)
                elif t == "*":
                    b = int(stack.pop())
                    a = int(stack.pop())
                    stack.append(a*b)
                elif t == "/":
                    b = int(stack.pop())
                    a = int(stack.pop())
                    stack.append(a/b)
            else:
                stack.append(t)

        return int(stack[0])
