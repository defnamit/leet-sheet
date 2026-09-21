# **3524. Find X Value of Array I**



You are given an array of positive integers nums, and a positive integer k.

You are allowed to perform an operation once on nums, where in each operation you can remove any non-overlapping prefix and suffix from nums such that nums remains non-empty.

You need to find the x-value of nums, which is the number of ways to perform this operation so that the product of the remaining elements leaves a remainder of x when divided by k.

Return an array result of size k where result[x] is the x-value of nums for 0 <= x <= k - 1.

A prefix of an array is a subarray that starts from the beginning of the array and extends to any point within it.

A suffix of an array is a subarray that starts at any point within the array and extends to the end of the array.

Note that the prefix and suffix to be chosen for the operation can be empty.

# MY EXPLANATION-



1. `dp[r]` means **how many subarrays ending at the previous index have product `% k = r`**.
2. When we get a new number `x`, we create `new_dp` for subarrays ending at `x`.
3. The single-element subarray `[x]` has remainder `x % k`, so `new_dp[x % k] += 1`.
4. Every old subarray can be extended by `x`.
5. If its old remainder is `r`, the new remainder becomes **`(r * x) % k`**.
6. So we do `new_dp[(r*x) % k] += dp[r]` for every possible `r`.
7. Add `new_dp` to `ans` because these are all the new subarrays ending at this position.
8. Finally, `dp = new_dp`, because these subarrays become the **previous subarrays** for the next number.
