class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        slen, tlen = len(s), len(t)
        dp = [0] * tlen + [1]
        for i in range(slen - 1, -1, -1):
            start_j = max(0, tlen - slen + i)
            end_j = min(tlen - 1, i)
            for j in range(start_j, end_j + 1):
                if s[i] == t[j]:
                    dp[j] += dp[j + 1]
        return dp[0]
