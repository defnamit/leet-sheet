class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        if s == ''.join(sorted(s)):
            return 0

        if n == 2:
            return -1

        minm = min(s)
        maxm = max(s)

        if s[0] == minm or s[-1] == maxm:
            return 1

        if any(c == minm or c == maxm for c in s[1:-1]):
            return 2

        return 3
