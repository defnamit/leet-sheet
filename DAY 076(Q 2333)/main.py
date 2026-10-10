class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if k >= sum(diff):
            return 0

        left, right = 0, max(diff)

        while left < right:
            mid = (left + right) // 2
            need = sum(max(0, x - mid) for x in diff)

            if need <= k:
                right = mid
            else:
                left = mid + 1

        remaining = k - sum(max(0, x - left) for x in diff)
        diff = [min(x, left) for x in diff]

        for i in range(len(diff)):
            if remaining == 0:
                break
            if diff[i] == left and left > 0:
                diff[i] -= 1
                remaining -= 1

        return sum(x * x for x in diff)
