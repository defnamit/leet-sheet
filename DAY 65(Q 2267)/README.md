# **2267. Check if There Is a Valid Parentheses String Path**



A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

It is ().
It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
It can be written as (A), where A is a valid parentheses string.
You are given an m x n matrix of parentheses grid. A valid parentheses string path in the grid is a path satisfying all of the following conditions:

The path starts from the upper left cell (0, 0).
The path ends at the bottom-right cell (m - 1, n - 1).
The path only ever moves down or right.
The resulting parentheses string formed by the path is valid.
Return true if there exists a valid parentheses string path in the grid. Otherwise, return false.



# MY EXPLANATION-


So our main aim throughout the whole process of solving this question is to make count(k) == 0 , because k counts total number of open braces , and while we reach at the end (m-1,n-1) we want all the braces to be closed to return True.


Cache is imported and important because , it is basically a temporary storage area. Without cache our recursive function will not be able to keep the tracks of every path , suppose reaching at a particular destination (m-1,n-1) has several paths , and cache helps here to recognize which path returns False and which returns True , so we dont have to count again and again and increase our execution time.


In boundary checks , we want that our steps to the path should not be odd because in that case we will left with a non paired brace , we should not have a closed brace in start and an open brace at the end , that immediately returns False , because these will create anomaly .


Then we will run a recursive function with i=row , j = column we are currently in , k= count of open braces.


(FIRST BASE CASE) #As we will iterate in our 2d array , and as we encounter an open brace we will increase our count and with closing brace we will decrease our count.


(SECOND BASE CASE) #Most important cases , our count should never be 0 , if its 0 that means we are in wrong path because we encountered more closed braces than open braces.
k > m - i + n - j - 1 , This basically is tracking that our opened braces should never be greater than the paths left to reach corner of the array , (because we need to close our brace at the corner , and if the steps are not equal to the count(k) that means we will never be able to close our opened braces and our path is incorrect)


(THIRD BASE CASE) #If we finally reached at the corner and our count==0 that means we have valid path , so return true else false.



We have initialized result(res) = False , that means till now we haven't reached any valid path.




Below is the flowchart , that will help you understand whole recursion steps:


Try DOWN
   ↓
Does it work?
   ↓
YES → return True
NO
   ↓
Try RIGHT
   ↓
Does it work?
   ↓
YES → return True
NO → return False



Main thing is "not res" , so basically here we dont want to enter that path that already returns True , because why would we enter the path which we already entered in previous recursions (and found it invalide in further steps) , so we will be looking for that path only which we never visited.


At last we will print our result.