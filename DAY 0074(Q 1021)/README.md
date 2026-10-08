# **1021. Remove Outermost Parentheses**


A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.




# MY EXPLANATION-


Here we will be using stack , but only to append the valid parenthesis only (inner one).

How to check validity , if we encounter any of the "(" or ")" , and our count (that is count of opening parenthesis "(" ) is greater than 1 , that means one "(" is still open and we are currently in the inner parenthesis .

So except that , we will append all valid parenthesis in the stack , and then "".join(res) this will convert it back to string
