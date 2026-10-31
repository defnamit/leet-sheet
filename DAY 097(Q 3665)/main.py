from functools import lru_cache
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        
        @lru_cache(None)
        def dfs(a, b, direct):

            if a < 0 or a >= r or b < 0 or b >= c:
                return 0

            if a == r - 1 and b == c - 1:
                return 1

            if grid[a][b] == 1:

                if direct == "right":
                    return dfs(a + 1, b, "down")

                if direct == "down":
                    return dfs(a, b + 1, "right")

            return (dfs(a, b + 1, "right") + dfs(a + 1, b, "down")) % (10**9 + 7)

        return dfs(0,0,"start")
