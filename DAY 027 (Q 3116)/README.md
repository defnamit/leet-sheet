## **3116. Kth Smallest Amount With Single Denomination Combination**





**You are given an integer array coins representing coins of different denominations and an integer k.**



**You have an infinite number of coins of each denomination. However, you are not allowed to combine coins of different denominations.**



**Return the kth smallest amount that can be made using these coins.**







## **MY EXPLANATION-**



**Here is how the solution works in 6 key lines:**



**1. \*\*Binary Search\*\*: We search for the answer in the range $\[1, \\text{min}(\\text{coins}) \\times k]$.**

**2. \*\*Subset Iteration\*\*: We iterate through all $2^N - 1$ subset combinations of the given coin denominations.**

**3. \*\*Least Common Multiple\*\*: For each subset, we compute the $\\text{LCM}$ of all its coins.**

**4. \*\*Inclusion-Exclusion\*\*: We add $\\lfloor x / \\text{LCM} \\rfloor$ for odd-sized subsets and subtract it for even-sized subsets to count unique multiples $\\le x$.**

**5. \*\*Adjusting Bounds\*\*: If the count of valid amounts is at least $k$, we try a smaller candidate number; otherwise, we search higher.**

**6. \*\*Final Result\*\*: The lowest number $x$ that yields at least $k$ valid multiples is our answer.**

