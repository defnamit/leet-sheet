# 3302\. Find the Lexicographically Smallest Valid Sequence



You are given two strings word1 and word2.



A string x is called almost equal to y if you can change at most one character in x to make it identical to y.



A sequence of indices seq is called valid if:



The indices are sorted in ascending order.

Concatenating the characters at these indices in word1 in the same order results in a string that is almost equal to word2.

Return an array of size word2.length representing the lexicographically smallest valid sequence of indices. If no such sequence of indices exists, return an empty array.



Note that the answer must represent the lexicographically smallest array, not the corresponding string formed by those indices.



&#x20;

# MY EXPLANATION-



1\. The code finds indices in `word1` that can form `word2` as a subsequence, allowing \*\*at most one mismatched character\*\*.

2\. `last` stores the latest possible index in `word1` where each character of `word2` can be matched.

3\. It calculates `last` by scanning `word1` and `word2` \*\*from right to left\*\*.

4\. Then it scans `word1` from left to right and greedily picks matching characters.

5\. If a character doesn't match, it can use the \*\*one allowed mismatch\*\*, but only if the remaining characters of `word2` can still be matched.

6\. Finally, it returns the selected indices if all characters are matched; otherwise, it returns `\[]`.







