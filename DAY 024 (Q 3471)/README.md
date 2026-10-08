# **3471. Find the Largest Almost Missing Integer**





**You are given an integer array nums and an integer k.**



**An integer x is almost missing from nums if x appears in exactly one subarray of size k within nums.**



**Return the largest almost missing integer from nums. If no such integer exists, return -1.**



**A subarray is a contiguous sequence of elements within an array.**





## ***MY EXPLANATION-***

&#x20;   



**1. `count` stores \*\*how many length-`k` subarrays contain each number\*\*.**

**2. The outer loop `i` moves through every possible starting position of a length-`k` subarray.**

**3. `seen` stores the \*\*unique elements\*\* of the current subarray.**

**4. We use a `set` because if `\[0,0]` is a subarray, `0` should be counted \*\*once for that subarray\*\*, not twice.**

**5. `count\[x] += 1` means: \*\*number `x` appeared in one more length-`k` subarray\*\*.**

**6. Finally, `count\[x] == 1` means `x` appears in \*\*exactly one subarray\*\*.**

**7. `max(ans, x)` keeps the \*\*largest\*\* such number; if none exists, `ans` remains `-1`.**





