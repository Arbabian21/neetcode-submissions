class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == "+":
                val1, val2 = stack.pop(), stack.pop()
                stack.append(val1 + val2)
            elif char == "-":
                val1, val2 = stack.pop(), stack.pop()
                stack.append(val2 - val1)
            elif char == "*":
                val1, val2 = stack.pop(), stack.pop()
                stack.append(val1 * val2)
            elif char == "/":
                val1, val2 = stack.pop(), stack.pop()
                stack.append(int(val2/val1))
            
            else:
                stack.append(int(char))

        return 0 if not stack else stack[-1]