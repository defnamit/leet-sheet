# **3310. Remove Methods From Project**





You are maintaining a project that has n methods numbered from 0 to n - 1.



You are given two integers n and k, and a 2D integer array invocations, where invocations\[i] = \[ai, bi] indicates that method ai invokes method bi.



There is a known bug in method k. Method k, along with any method invoked by it, either directly or indirectly, are considered suspicious and we aim to remove them.



A group of methods can only be removed if no method outside the group invokes any methods within it.



Return an array containing all the remaining methods after removing all the suspicious methods. You may return the answer in any order. If it is not possible to remove all the suspicious methods, none should be removed.



## **MY EXPLANATION-**



**1. `adj` creates an \*\*adjacency list\*\*, where `adj\[u]` stores all methods called by method `u`.**

**2. Starting from method `k`, the BFS finds every method that can be reached from `k`; these are stored in `suspicious`.**

**3. `queue` is used to process suspicious methods one by one and discover more suspicious methods.**

**4. The second loop checks if a \*\*non-suspicious method calls a suspicious method\*\*; if so, we cannot safely remove the suspicious methods, so `range(n)` is returned.**

**5. Otherwise, all suspicious methods can be removed, so the code returns only the methods \*\*not present in `suspicious`\*\*.**

**6. In short: \*\*find all methods affected by `k`, check whether anything outside calls them, then decide whether to remove them.\*\***



