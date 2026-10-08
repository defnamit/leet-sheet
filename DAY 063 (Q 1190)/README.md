# **1190. Reverse Substrings Between Each Pair of Parentheses**



You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.



# MY EXPLANATION-


First while condition is written , because we are reversing the substrings inside the bracket , simultaneously removing brackets too , and if in the string s any bracket is present that means there are still some operation need to perform.


We will use two pointer method , start pointer at the end of the string and end pointer at the beginning .


Our start pointer will find the first "(" in s , because if it is starting from backside and encounters any opening braces that means we are at the right position , that is in the inner braces.


Will place our end after the start found its position , because its closing brace will be in front only .


And when we will get our desired position we used this formula, s = s[:start] + s[start + 1:end][::-1] + s[end + 1:]

This basically does is that keeps the substring as it is back at the start and back at end , and the substring we have to perform reverse operation we will sliced and then [::-1] is used to reverse that particular substring.


And the while loop will go on and on , until we remove all the braces , meaning we reverse every substring according to the rule.

