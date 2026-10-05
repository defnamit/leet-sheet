class Solution(object):
    def scoreOfParentheses(self, s):
        
        stack = []

        for i in s:

            if i == "(":
                stack.append(i)

            elif i == ")":

                if stack[-1] == "(":
                    stack.pop()

                    if stack and isinstance(stack[-1], int):
                        last = stack.pop()
                    else:
                        last = 0

                    stack.append(last + 1)

                else:
                    last = stack.pop()
                    stack.pop()       

                    if stack and isinstance(stack[-1], int):
                        previous = stack.pop()
                    else:
                        previous = 0

                    stack.append(previous + 2 * last)

        return stack[0]
