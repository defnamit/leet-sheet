import math


class Solution:

  def findKthSmallest(self, coins: list[int], k: int) -> int:
    n = len(coins)

    def count_valid(x: int) -> int:
      """Returns how many valid amounts are <= x using Inclusion-Exclusion."""
      cnt = 0
      # Bitmask over all 2^n - 1 non-empty subsets
      for mask in range(1, 1 << n):
        lcm_val = 1
        bits = 0
        for i in range(n):
          if (mask >> i) & 1:
            bits += 1
            lcm_val = math.lcm(lcm_val, coins[i])
            if lcm_val > x:
              break

        if bits % 2 == 1:
          cnt += x // lcm_val
        else:
          cnt -= x // lcm_val
      return cnt

    # Binary search boundaries
    low, high = 1, min(coins) * k
    ans = high

    while low <= high:
      mid = (low + high) // 2
      if count_valid(mid) >= k:
        ans = mid
        high = mid - 1  # Try to find a smaller valid x
      else:
        low = mid + 1

    return ans
