## **1510. Stone Game IV**



**Alice and Bob take turns playing a game, with Alice starting first.**



**Initially, there are n stones in a pile. On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.**



**Also, if a player cannot make a move, he/she loses the game.**



**Given a positive integer n, return true if and only if Alice wins the game otherwise return false, assuming both players play optimally.**





## **MY EXPLANATION-**



**1. `dp\[i]` tells whether the \*\*current player can win\*\* when there are `i` stones remaining.**

**2. Initially, all values are `False`, meaning losing positions.**

**3. For each `i`, the player tries removing every possible \*\*perfect square\*\* (`1, 4, 9, ...`).**

**4. If removing a square leaves a position where the opponent \*\*cannot win\*\* (`dp\[i - j\*j] == False`), then `dp\[i] = True`.**

**5. The `break` stops checking once a winning move is found.**

**6. Finally, `dp\[n]` tells whether \*\*Alice (the first player) wins\*\*.**



