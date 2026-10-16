from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7

        tree = [0] * (4 * n)
        sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def push(node, start, end):
            if lazy[node] == 0:
                return

            v = lazy[node]
            mid = (start + end) // 2

            for child, length in (
                (2 * node + 1, mid - start + 1),
                (2 * node + 2, end - mid)
            ):
                sq[child] = (
                    sq[child] + 2 * v * tree[child] + length * v * v
                ) % MOD
                tree[child] = (tree[child] + length * v) % MOD
                lazy[child] += v

            lazy[node] = 0

        def update(node, start, end, l, r):
            if r < start or end < l:
                return

            if l <= start and end <= r:
                length = end - start + 1
                v = 1

                sq[node] = (
                    sq[node] + 2 * v * tree[node] + length * v * v
                ) % MOD
                tree[node] = (tree[node] + length * v) % MOD
                lazy[node] += v
                return

            push(node, start, end)
            mid = (start + end) // 2

            update(2 * node + 1, start, mid, l, r)
            update(2 * node + 2, mid + 1, end, l, r)

            tree[node] = (
                tree[2 * node + 1] + tree[2 * node + 2]
            ) % MOD
            sq[node] = (
                sq[2 * node + 1] + sq[2 * node + 2]
            ) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            p = last.get(x, -1)
            update(0, 0, n - 1, p + 1, i)
            ans = (ans + sq[0]) % MOD
            last[x] = i

        return ans
