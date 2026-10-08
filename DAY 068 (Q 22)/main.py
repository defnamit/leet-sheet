class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        result = []

        def backtrack(path, open, close):

            if len(path) == 2 * n:
                result.append(path)
                return

            if open < n:
                backtrack(path + "(", open + 1, close)

            if close < open:
                backtrack(path + ")", open, close + 1)

        backtrack("", 0, 0)

        return result
