class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):

        n = len(nums)

        # value + original index
        arr = []
        for i in range(n):
            arr.append((nums[i], i))

        # Sort according to value
        arr.sort()

        ans = nums[:]

        i = 0

        while i < n:

            # Find all values connected to nums[i]
            j = i
            while j + 1 < n:
                if arr[j + 1][0] - arr[j][0] <= limit:
                    j += 1
                else:
                    break
            # Take values and their original positions
            values = []
            indices = []

            for k in range(i, j + 1):
                values.append (arr[k][0])
                indices.append(arr[k][1])

            # Smallest values should go to smallest indices
            indices.sort()

            for k in range(len(values)):
                ans[indices[k]] = values[k]

            # Move to next group
            i = j + 1

        return ans
