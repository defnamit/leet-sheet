# **2029. Stone Game IX**





### Alice and Bob continue their games with stones. There is a row of n stones, and each stone has an associated value. You are given an integer array stones, where stones\[i] is the value of the ith stone.

### 

### Alice and Bob take turns, with Alice starting first. On each turn, the player may remove any stone from stones. The player who removes a stone loses if the sum of the values of all removed stones is divisible by 3. Bob will win automatically if there are no remaining stones (even if it is Alice's turn).

### 

### Assuming both players play optimally, return true if Alice wins and false if Bob wins.













## **MY EXPLANATION-**



**1. Group all stones according to their remainder when divided by `3`: `0`, `1`, or `2`.**

**2. A player loses when their chosen stone makes the running sum divisible by `3`.**

**3. Stones with remainder `0` don't change the remainder, so only their \*\*parity\*\* matters.**

**4. If there are no remainder-`1` or remainder-`2` stones, Alice cannot win.**

**5. When the number of remainder-`0` stones is even, Alice wins if both remainder `1` and `2` groups exist.**

**6. When it is odd, Alice wins only when `abs(cnt\[1] - cnt\[2]) > 2`.**



