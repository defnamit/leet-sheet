# **3518. Smallest Palindromic Rearrangement II**





## You are given a palindromic string s and an integer k.

## Return the k-th lexicographically smallest palindromic permutation of s. If there are fewer than k distinct palindromic permutations, return an empty string.

## Note: Different rearrangements that yield the same palindromic string are considered identical and are counted once.





## **MY EXPLANATION-**



**1. `Counter(s)` counts how many times each character appears in the string.**

**2. `half` stores half of each character's frequency because a palindrome has matching characters on both sides.**

**3. `mid` stores the character with an odd frequency, which goes in the center.**

**4. `count\_perm()` calculates how many unique arrangements can be made from the characters in `half`.**

**5. `math.comb()` is used to efficiently count arrangements when characters are repeated.**

**6. If the total number of possible arrangements is less than `k`, the function returns `""`.**

**7. The left half is constructed greedily by trying characters from smallest to largest.**

**8. For each character, `ways` calculates how many valid arrangements are possible if that character is selected.**

**9. If `ways < k`, those arrangements are skipped using `k -= ways`; otherwise, the character is kept.**

**10. Finally, the palindrome is formed as `left + mid + reverse(left)`.**



