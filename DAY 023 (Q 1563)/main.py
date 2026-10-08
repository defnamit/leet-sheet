class Solution(object):
    def stoneGameV(self, arr):

        if len(arr) <= 1:
            return 0

        ans = 0

        for i in range(len(arr) - 1):

            left = arr[:i+1]
            right = arr[i+1:]

            left_sum = sum(left)
            right_sum = sum(right)

            if left_sum < right_sum:
                ans = max(ans, left_sum + self.stoneGameV(left))

            elif left_sum > right_sum:
                ans = max(ans, right_sum + self.stoneGameV(right))

            else:
                ans = max(
                    ans,
                    left_sum + max(
                        self.stoneGameV(left),
                        self.stoneGameV(right)
                    )
                )

        return ans
