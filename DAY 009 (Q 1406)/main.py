class Solution(object):

  def stoneGameIII(self, sv):
    n = len(sv)
    memo = {}

    def dfs(i, j):

      if i > j:
        return 0
      if i == j:
        return sv[i]

      if (i, j) in memo:
        return memo[(i, j)]

      op1 = sv[i] - dfs(i + 1, j)

      op2 = (
          (sv[i] + sv[i + 1]) - dfs(i + 2, j)
          if i + 1 <= j
          else float("-inf")
      )

      op3 = (
          (sv[i] + sv[i + 1] + sv[i + 2]) - dfs(i + 3, j)
          if i + 2 <= j
          else float("-inf")
      )

      left = max((op1, op2, op3))

      memo[(i, j)] = left
      return left

    alice_advantage = dfs(0, n - 1)

    
    if alice_advantage > 0:
      return "Alice"
    elif alice_advantage < 0:
      return "Bob"
    else:
      return "Tie"
