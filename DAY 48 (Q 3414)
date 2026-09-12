class Solution:
    def maximumWeight(self, intervals):
        from bisect import bisect_right

        n = len(intervals)

        arr = []

        for i, (s, e, w) in enumerate(intervals):
            arr.append((s, e, w, i))

        arr.sort()

        starts = [x[0] for x in arr]

        # Find the next non-overlapping interval
        nxt = [0] * n

        for i in range(n):
            nxt[i] = bisect_right(starts, arr[i][1])

        # dp[i][k] = (maximum weight, indices)
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):

            for k in range(1, 5):

                # Don't take current interval
                skip = dp[i + 1][k]

                # Take current interval
                next_i = nxt[i]

                take_weight = arr[i][2] + dp[next_i][k - 1][0]

                take_indices = [arr[i][3]] + dp[next_i][k - 1][1]

                # ALWAYS keep indices sorted
                take_indices.sort()

                if take_weight > skip[0]:
                    dp[i][k] = (take_weight, take_indices)

                elif take_weight < skip[0]:
                    dp[i][k] = skip

                else:
                    # Same weight → lexicographically smaller indices
                    dp[i][k] = (
                        take_weight,
                        min(skip[1], take_indices)
                    )

        return dp[0][4][1]
