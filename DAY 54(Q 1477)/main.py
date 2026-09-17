class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')

        # best[i] = minimum length of a target-sum subarray
        # completely contained in arr[0:i+1]
        best = [INF] * n

        left = 0
        total = 0
        shortest = INF
        ans = INF

        for right in range(n):
            total += arr[right]

            while total > target:
                total -= arr[left]
                left += 1

            if total == target:
                length = right - left + 1

                # A previous valid subarray must end before `left`
                if left > 0 and best[left - 1] != INF:
                    ans = min(ans, length + best[left - 1])

                shortest = min(shortest, length)

            best[right] = shortest

        return -1 if ans == INF else ans
