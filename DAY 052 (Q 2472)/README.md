# **2472. Maximum Number of Non-overlapping Palindrome Substrings**





You are given a string s and a positive integer k.



Select a set of non-overlapping substrings from the string s that satisfy the following conditions:



The length of each substring is at least k.

Each substring is a palindrome.

Return the maximum number of substrings in an optimal selection.



A substring is a contiguous sequence of characters within a string.



&#x20;



# MY EXPLANATION-



1\. `pal\[i]\[j]` stores whether the substring from index `i` to `j` is a palindrome.

2\. We check this using `s\[i] == s\[j]` and whether the inner substring is also a palindrome.

3\. `j-i < 2` handles palindromes of length 1 or 2.

4\. `dp\[i]` stores the maximum number of valid non-overlapping palindromes using the first `i` characters.

5\. For every starting index `i`, we try every ending index `j` where the length is at least `k`.

6\. If `s\[i:j+1]` is a palindrome, we update `dp\[j+1] = max(dp\[j+1], dp\[i] + 1)`.

7\. Finally, `dp\[n]` gives the maximum number of non-overlapping palindromes.



