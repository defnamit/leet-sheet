class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        r = len(grid)
        c = len(grid[0])
        count = 0

        def dfs(i, j):
            if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] == 0:
                return 0

            s = grid[i][j]
            grid[i][j] = 0

            s += dfs(i + 1, j)
            s += dfs(i - 1, j)
            s += dfs(i, j + 1)
            s += dfs(i, j - 1)

            return s

        for i in range(r):
            for j in range(c):
                if grid[i][j] != 0:
                    a = dfs(i, j)

                    if a % k == 0:
                        count += 1

        return count
