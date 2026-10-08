# **1621. Number of Sets of K Non-Overlapping Line Segments**





Given n points on a 1-D plane, where the ith point (from 0 to n-1) is at x = i, find the number of ways we can draw exactly k non-overlapping line segments such that each segment covers two or more points. The endpoints of each segment must have integral coordinates. The k line segments do not have to cover all n points, and they are allowed to share endpoints.

Return the number of ways we can draw k non-overlapping line segments. Since this number can be huge, return it modulo 109 + 7.


&#x20;



# MY EXPLANATION-



If you analyze question properly you will know we will be using combination formula

We have actually total n+k-1 total possibilities,
How? Number of ways to distribute x identical things among m places is: n+k-1.|

From that we have to chose 2k thinks , because every line will have two endings , and total lines we will be having is k number of lines.

So by math.comb(n+k-1,2k) we can get the answer. (and modulo too)


