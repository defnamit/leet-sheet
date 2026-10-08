# **115. Distinct Subsequences**



Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.


# MY EXPLANATION-


1. `x` moves **forward** through `s`, but for each fixed `x`, `j` moves **backward** through `t` — they are not moving at the same time.

2. Suppose `s = "bb"` and `t = "bb"`; when we process the first `b`, we have `x = 'b'`.

3. Initially `f = [1,0,0]`, meaning: `f[0]=1` way to make `""`, `f[1]=0` ways to make `"b"`, `f[2]=0` ways to make `"bb"`.

4. If we moved `j` **forward**, we would first do `f[1] += f[0]`, giving `f = [1,1,0]`.

5. Then we would move to `j=1` and do `f[2] += f[1]`.

6. But `f[1]` now contains the result created using the **same current `b`**, so we would use that `b` again.

7. That means one character of `s` would be used twice: `b → t[0]` and the **same** `b → t[1]` ❌.

8. By moving backward, we first check `j=1`, then `j=0`, so when calculating `f[2]`, `f[1]` still contains its **old value**.

9. Only after that do we update `f[1]`, so the current `x` cannot immediately reuse its own update.

10. **Therefore, `j` moves backward because 1D DP reuses the same `f` array, and backward movement prevents the current character `x` from being counted more than once.**
