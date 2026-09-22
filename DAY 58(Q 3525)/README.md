# **3525. Find X Value of Array II**



You are given an array of positive integers nums and a positive integer k. You are also given a 2D array queries, where queries[i] = [indexi, valuei, starti, xi].

You are allowed to perform an operation once on nums, where you can remove any suffix from nums such that nums remains non-empty.

The x-value of nums for a given x is defined as the number of ways to perform this operation so that the product of the remaining elements leaves a remainder of x modulo k.

For each query in queries you need to determine the x-value of nums for xi after performing the following actions:

Update nums[indexi] to valuei. Only this step persists for the rest of the queries.
Remove the prefix nums[0..(starti - 1)] (where nums[0..(-1)] will be used to represent the empty prefix).
Return an array result of size queries.length where result[i] is the answer for the ith query.

A prefix of an array is a subarray that starts from the beginning of the array and extends to any point within it.

A suffix of an array is a subarray that starts at any point within the array and extends to the end of the array.

Note that the prefix and suffix to be chosen for the operation can be empty.

Note that x-value has a different definition in this version.


# MY EXPLANATION-



1. **Goal:** Count non-empty prefixes in $nums[start..n-1]$ whose product modulo $k$ equals $x$, with dynamic updates.
2. **Key Constraint:** Since modulo k is tiny (1 <= k <= 5), we can track all k possible remainder counts directly.
3. **Data Structure:** Use a **Segment Tree** where each node represents a range of the array.
4. **Node State:** Each node stores the segment's **total product modulo $k$** and an array `cnt` of length $k$.
5. **Prefix Tracking:** `cnt[r]` stores the number of prefixes within the node's range that have a product $\pmod k = r.
6. **Merging Left & Right:** Left prefixes stay as-is: `res.cnt[r] = left.cnt[r]`.
7. **Cross-Boundary Prefixes:** Prefixes crossing into the right child take `left.prod` times a right prefix's product: $(left.prod \times r_R) \pmod k$.
8. **Point Updates:** Updating $nums[index] = value$ takes $O(k \log n)$ time by refreshing segment tree nodes up to the root.
9. **Range Query:** Querying $[start, n-1]$ returns a merged node holding prefix remainder counts for that entire suffix.
10. **Efficiency:** Total time per query is $O(k \log n)$, which easily passes within competitive limits.