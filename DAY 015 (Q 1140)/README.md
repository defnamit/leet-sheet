# **1140. Stone Game II**



**Alice and Bob continue their games with piles of stones. There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles\[i]. The objective of the game is to end with the most stones.**



**Alice and Bob take turns, with Alice starting first.**



**On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M. Then, we set M = max(M, X). Initially, M = 1.**



**The game continues until all the stones have been taken.**



**Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.**



## **MY EXPLANATION-**



**1. `suffix\_sum` stores the total stones from each index to the end, so we can quickly calculate remaining stones.**

**2. `dfs(i, m)` calculates the \*\*maximum stones the current player can collect\*\* starting at index `i` with limit `m`.**

**3. If the player can take all remaining piles (`i + 2\*m >= n`), they simply take all of them.**

**4. Otherwise, the player tries taking `x` piles, where `x` ranges from `1` to `2\*m`.**

**5. `opponent\_score` calculates how many stones the opponent can get afterward, so `current\_score = remaining stones - opponent's score`.**

**6. `memo` stores previously calculated `(i, m)` states to avoid repeated calculations, and `dfs(0,1)` gives the final maximum stones.**







