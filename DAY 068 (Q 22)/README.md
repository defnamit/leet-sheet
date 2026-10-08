# **22. Generate Parentheses**



Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


# MY EXPLANATION-


We will use recursive function , because recursion is the only method i think can generate all valid patterns based on the condition.

First if , trying to verify that if number of closing brackets = opening brackets (that is 2n) , then we have a valid pattern , and will append directly in the list.

Second if, if number of opening brackets is less than n , that means we have to open more brackets using recursion , so as to match the valid pattern.

Third if , number of closed bracket is less than open one , means there are still some opened brackets and have to recurse the function.

How will it create a pattern? If we have "(" in first recursion , then in second recursion we have two choices that whether to close that bracket or open another open , we will open because of the order of recursion command , and as the opening recursion ends , then we can close the brackets , and by adding all these opening and closing pattern or combination we can get all the valid strings.



(FUN FACT- I calculated a formula for to know how many patterns can exist based on the number of brackets that is = combination(2n , n+1).