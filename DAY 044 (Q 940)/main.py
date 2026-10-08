class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        dp = [0] * 26

        for ch in s:
            i = ord(ch) - ord('a')

            total = sum(dp) + 1

            dp[i] = total % MOD

        return sum(dp) % MOD
