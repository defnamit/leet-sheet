import math

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        def solve(nums):
            if len(nums) <= 2:
                return 1

            root = nums[0]
            l = []
            r = []

            for i in nums[1:]:
                if i > root:
                    r.append(i)
                else:
                    l.append(i)

            n = len(l)
            combination = math.comb(len(nums) - 1, n)

            return (combination * solve(l) * solve(r)) % MOD

        return (solve(nums) - 1) % MOD
