class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        n = len(nums)

        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        point = 0
        maximum = nums[0]

        while point < n:
            maximum = max(maximum, nums[point])

            minimum = suffix_min[point]

            score = maximum - minimum

            if score <= k:
                return point

            point += 1

        return -1
