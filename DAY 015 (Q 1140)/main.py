class Solution(object):
    def stoneGameII(self, piles):
      
        n = len(piles)
        
        
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        memo = {}

        def dfs(i, m):
            
            if i + 2 * m >= n:
                return suffix_sum[i]
            
            
            if (i, m) in memo:
                return memo[(i, m)]
            
            max_stones = 0
            
            for x in range(1, 2 * m + 1):
                
                opponent_score = dfs(i + x, max(m, x))
                current_score = suffix_sum[i] - opponent_score
                max_stones = max(max_stones, current_score)
                
            memo[(i, m)] = max_stones
            return max_stones
        
        return dfs(0, 1)
