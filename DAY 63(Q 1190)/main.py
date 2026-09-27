class Solution:
    def reverseParentheses(self, s: str):

        while "(" in s:

            start = len(s) - 1
            end = 0

            # Find the rightmost '('
            while s[start] != "(":
                start -= 1

            # Find the first ')' after it
            end = start + 1

            while s[end] != ")":
                end += 1

            # Reverse the characters between '(' and ')'
            s = s[:start] + s[start + 1:end][::-1] + s[end + 1:]

        return s
