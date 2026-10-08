# **301. Remove Invalid Parentheses**


Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.





# MY EXPLANATION-


1. `isValid()` checks whether a string has properly matched `(` and `)` using `count`.
2. `count++` for `(` and `count--` for `)`.
3. If `count` becomes negative, there is an unmatched `)`, so the string is invalid.
4. At the end, `count` must be `0` for the string to be valid.
5. `queue = deque([s])` starts BFS with the original string.
6. BFS works level by level: **0 removals → 1 removal → 2 removals → ...**
7. For every string, we try removing each `(` or `)` using `curr[:i] + curr[i+1:]`.
8. `visited` prevents us from processing the same string multiple times.
9. When a valid string is found, we add it to `answer`; because BFS is level-by-level, this is the **minimum-removal level**.
10. Once `answer` is non-empty, we `break` and return all valid strings from that level.
