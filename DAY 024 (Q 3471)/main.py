from collections import Counter

class Solution(object):
    def largestInteger(self, nums, k):

        n = len(nums)
        count = Counter()

        # Check every subarray of length k
        for i in range(n - k + 1):
            seen = set()

            for j in range(i, i + k):
                seen.add(nums[j])

            for x in seen:
                count[x] += 1

        ans = -1

        for x in count:
            if count[x] == 1:
                ans = max(ans, x)

        return ans
