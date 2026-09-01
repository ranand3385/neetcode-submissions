class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oper = set(['+', '-', '*', '/'])
        stack = []

        for token in tokens:
            if token not in oper:
                stack.append(int(token))
            else:
                if len(stack) >= 2:
                    if token == '+':
                        newVal = (stack[-2] + stack[-1])
                        stack.pop()
                        stack.pop()
                        stack.append(newVal)
                    elif token == '-':
                        newVal = (stack[-2] - stack[-1])
                        stack.pop()
                        stack.pop()
                        stack.append(newVal)
                    elif token == '*':
                        newVal = (stack[-2] * stack[-1])
                        stack.pop()
                        stack.pop()
                        stack.append(newVal)
                    else:
                        newVal = int(float(stack[-2]) / stack[-1])
                        stack.pop()
                        stack.pop()
                        stack.append(newVal)
        return stack[0]

        