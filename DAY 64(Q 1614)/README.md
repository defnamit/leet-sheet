# **1614. Maximum Nesting Depth of the Parentheses**



Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.



# MY EXPLANATION-


The two variables will be used , count is used to count number of open braces , depth is used to find the most inner (deep) braces.


Will use for loop in s , we will increase count whenever we will encounter "(" because to go to the inner brace we have to know that how much braces we have passed .

And as soon as we encounter ")" close brace , this is a signal that we may be in the innermost brace or may be not , that is why we will use max operator to atleast store the most deep brace , and in the next step we will also decrease the count by 1 , because the braces are now closed.


At last when the loop will completely iterate we will get the answer.