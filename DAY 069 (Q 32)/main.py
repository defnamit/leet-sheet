CODE 1-

'''class Solution:
    def longestValidParentheses(self, s: str) -> int:

        stack = []
        lst = []

        def replace(lst):
            for i in range(len(lst) - 1, -1, -1):
                if lst[i] == 0:
                    lst[i] = 1
                    break

        if s is None:
            return 0

        for i in range(len(s)):

            if s[i] == "(":
                stack.append(s[i])
                lst.append(0)

            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                    replace(lst)
                    lst.append(1)

                else:
                    lst.append(0)

        count = 0
        m = 0

        for i in range(len(lst)):
            if lst[i] == 1:
                count += 1
            else:
                m = max(m, count)
                count = 0

        m = max(m, count)'''

  CODE 2-

  class Solution:
    def longestValidParentheses(self, s):
        stack = [-1]
        max_length = 0

        for i in range(len(s)):

            if s[i] == '(':
                stack.append(i)

            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])

        return max_length

        return m
