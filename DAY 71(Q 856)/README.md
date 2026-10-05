# **856. Score of Parentheses**



Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.


# MY EXPLANATION-


I evaluated this crazy method with less space and less time , using only one stack , we can find the answer.

So first let me explain an abstract idea of what my code is overall doing.

= So will append an open "(" and pop when encountered its pair ")" that is the classical way we were doing from previous questions too , but the main catch is as soon we will pop the "(" we will add 1 too in the stack , because it tells the outer parenthesis that we closed 1 inner parenthesis , and condition for appending 1 is only when the last element in stack is "(" , but if we pop "(" and encounter an integer we will add both numbers , because encountering that integer is telling us that the parenthesis pairs are of the same outer parenthesis.

If we encounter ")" and int value as the last element , will first pop that int and store it and then remove its pair "(" from the stack , and then we will check after popping "(" that we dont have int value as last element , if there is we will again add it because as mentioned above it is of same parenthesis , but we will multiply our stored int with 2 also , because as mentioned in ques for the situation of non empty parenthesis.

After performing all operation we will be left with only our answer in the stack , because all of its "(" is removed because expression is balanced.



And now if you will look in the code you will understand what my code is doing ,
#isinstance(stack[-1],int) , is used to return True or False , if last element in the Stack is int.