class Solution:
    def resultArray(self, nums, k):
        ans = [0] * k
        dp = [0] * k

        for x in nums:
            new_dp = [0] * k

            # Subarray containing only x
            new_dp[x % k] += 1

            # Extend all previous subarrays
            for r in range(k):
                new_r = (r * x) % k
                new_dp[new_r] += dp[r]

            # Add subarrays ending here to answer
            for r in range(k):
                ans[r] += new_dp[r]

            dp = new_dp

        return ans
