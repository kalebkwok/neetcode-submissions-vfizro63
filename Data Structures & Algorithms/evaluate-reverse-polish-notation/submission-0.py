class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "-", "*", "/"}
        for s in tokens:
            if s in operations:
                a, b = int(stack.pop()), int(stack.pop())
                if s == "+":
                    stack.append(b + a)
                elif s == "-":
                    stack.append(b - a)
                elif s == "*":
                    stack.append(b * a)
                elif s == "/":
                    stack.append(b / a)
            else:
                stack.append(s)
        return int(stack[0])