# **921. Minimum Add to Make Parentheses Valid**


A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.




# MY EXPLANATION-


Our approach will be basically that , we will pop and append as usual in the stack as we did in previous questions , but the catch is whenever we encounter ")" but our stack is empty , that means we need its pair "(" , so in that case we will add +1 in count variable.

At last we need len(stack) with count because , there can be cases too where we have "(" but not its pair ")" , so the opening parenthesis will remain in the stack withut being popped , that is why we need len too.