# **1111. Maximum Nesting Depth of Two Valid Parentheses Strings**


A string is a valid parentheses string (denoted VPS) if and only if it consists of "(" and ")" characters only, and:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are VPS's, or
It can be written as (A), where A is a VPS.
We can similarly define the nesting depth depth(S) of any VPS S as follows:

depth("") = 0
depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's
depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

Given a VPS seq, split it into two disjoint subsequences A and B, such that A and B are VPS's (and A.length + B.length = seq.length). The subsequences may not necessarily be contiguous.

For example, for the sequence 123456789, one possible split is:

A = {1, 3, 5, 7, 9},

B = {2, 4, 6, 8}.

This corresponds to the output [0, 1, 0, 1, 0, 1, 0, 1, 0]  where 0 indicates membership in A and 1 indicates membership in B.

Now choose any such A and B such that max(depth(A), depth(B)) is the minimum possible value.

Return an answer array (of length seq.length) that encodes such a choice of A and B:  answer[i] = 0 if seq[i] is part of A, else answer[i] = 1.  Note that even though multiple answers may exist, you may return any of them.


# MY EXPLANATION-


So in ease let me tell what to do in this ques, So we have to divide all the braces in two groups , group 0 and group 1 and return it in a list form.


If the brace is in odd depth you have to place it in group 0 else group 1.

So our easy approach will be , if we encounter an open brace , we will increase our depth count , because obviously we are entering in depth and perform odd even operation to place in group 0 or 1.


But twist is , when we encounter a closed brace , we immediately are not coming out of the depth in that step only , thats why we first place that brace in group , then depth-1 because the closed brace is in the same depth of its paired open brace.

And thats how performing for loop on every brace will give you your suitable ans.
(In the questioned , it is mentioned that it can have multiple pattern of output , so whichever approach you find suitable is good for you , or else my way is lot more easier too.)
