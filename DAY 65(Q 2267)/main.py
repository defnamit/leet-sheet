from functools import cache

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Quick boundary checks
        if (m + n - 1) % 2 == 1 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
            
        @cache
        def dfs(i,j,k):
            # Update balance based on current cell
            if grid[i][j] == '(':
                k += 1 
            else:
                k-=1
    
            # invalid paths
            if k < 0 or k > m - i + n - j - 1:
                return False
                
            # Base case: reached bottom-right cell
            if i == m - 1 and j == n - 1:
                return k == 0
                
            # Move down or right
            res = False
            if i + 1 < m:
                res = res or dfs(i + 1, j, k)
            if not res and j + 1 < n:
                res = res or dfs(i, j + 1, k)
                
            return res

        return dfs(0, 0, 0)
