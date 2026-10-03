# **32. Longest Valid Parentheses**



Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

# MY EXPLANATION-


SO I WILL EXPLAIN YOU TWO APPROACH FOR THIS QUESTION , LONG ONE(FIRST) IS MY APPROACH , AND THE SECOND SHORT ONE IS THE MOST FEASIBLE ONE , YOU CAN UNDERSTAND BOTH FOR TO MAKE YOUR UNDERSTANDING STRONG.



SOLUTION 1-


We will be creating two lists , in stack we will store "(" and in lst we will store the pairs of valid substrings index by index as we move forward , it is acting kind of checkpoint.

Will run a for loop , if we find "(" , we will append that in stack and append 0 in lst , because it is still an unpaired parenthesis so we dont know yet that if its valid or invalid for now and for ahead.

If we find ")" and we already have an opening "(" ,so we found our pair and pop the "(" from stack , and as we found our valid pair we have to alter our lst from 0(invalid) to 1(valid) , for that we have already defined a replace function , which is just finding the first 0 from last and replacing it with 1.
And will be appending one more 1 in last after replace because , first 1 is counted for a valid opening bracket and second for valid closing bracket.

(Why first 0 from last? Because as you know the bracket that is opened first is always closed last , so if we encounter multiple inner brackets we will loose our track for first brackets , that is why replacing from last will help us to maintain that order.)


If we dont find any "(" for ")" that means we encountered our confirmed invalid pair , so we will append 0 in lst.


Now in lst , we have to find the maximum length of valid subarrays without any invalid substring in between, for that we will be adding length of all valid substrings (1+1+1...) until we encounter a 0 because that is an invalid and will create a boundary , so in that case we will use the max operator to find the maximum length of valid substring between the boundaries .




CODE 2-

1. `stack = [-1]` stores the **index of the last invalid boundary**; `-1` means before the string starts.
2. When we see `(`, we store its **index**: `stack.append(i)`.
3. When we see `)`, we `pop()` its matching `(` from the stack.
4. If the stack becomes empty, this `)` has no matching `(`, so we store its index as a **new boundary**.
5. Otherwise, `i - stack[-1]` gives the length of the current valid substring.
6. Example: for `"()"`, at `i=1`, `stack[-1]=-1`, so `1 - (-1) = 2`.
7. `max_length` keeps the largest valid length found so far.
8. **Your code marks valid positions using `0/1`; this code stores indices, so it can calculate the length directly without `lst`, `replace()`, or `2 * count`.**
