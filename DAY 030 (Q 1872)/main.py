class Solution(object):
    def stoneGameVIII(self, stones):

        n = len(stones)

        prefix = [0] * n
        prefix[0] = stones[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]

        ans = prefix[-1]

        for i in range(n - 2, 0, -1):
            ans = max(ans, prefix[i] - ans)

        return ans
