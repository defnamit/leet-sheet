# **678. Valid Parenthesis String**



Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".


# MY EXPLANATION-


Instead of checking opening parenthesis with single variable , we will be using two variables , because we never know that how the "*" in the string can be used (as an opening , closing or not to be used).


Encountering "(" , as always we will increase our count both in low and high , and in ")" we will decrease it.

Now when we encounter "*" , we will use as ")" in low counter and "(" in high counter , and add or subtract our count according to that.

If high ever went to negative , that means we encountered too many ")" and it is never possible to make it valid , that is why return False.

If low became negative , that means we used too many "*" as ")" , and we can make it nullify though because questions allows us for that , so we can make low again to 0, and if our count of low is 0 at the end of loop that means we encountered all valid parenthesis , if not that means we still have an opened "(".
