# 3348\. Smallest Divisible Digit Product II





You are given a string num which represents a positive integer, and an integer t.



A number is called zero-free if none of its digits are 0.



Return a string representing the smallest zero-free number greater than or equal to num such that the product of its digits is divisible by t. If no such number exists, return "-1".







## MY EXPLANATION-



1\. First, the code \*\*factorizes `t`\*\* into powers of `2, 3, 5, 7`, since digits `1–9` can only provide these prime factors.

2\. It stores the prime-factor contribution of each digit (`2 → 2`, `6 → 2×3`, `8 → 2³`, `9 → 3²`, etc.).

3\. It checks whether the original `num` already has enough factors to make its digit product divisible by `t`.

4\. If not, it goes \*\*from right to left\*\*, increasing one digit to find the smallest number greater than `num`.

5\. For the remaining positions, `enough()` checks whether the required factors can fit, while `build()` constructs the \*\*smallest possible suffix\*\*.

6\. If no number of the same length works, it creates the smallest valid number with \*\*one extra digit\*\*.



