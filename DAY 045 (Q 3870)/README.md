# **3870. Count Commas in Range**



You are given an integer n.



Return the total number of commas used when writing all integers from \[1, n] (inclusive) in standard number formatting.



In standard formatting:



A comma is inserted after every three digits from the right.

Numbers with fewer than 4 digits contain no commas.

&#x20;



# **MY EXPLANATION-**



you just have to tell the number of commas that will appear when you will reach that number n from 1.
First comma will come only after three digit only , so the smallest 3 digit is 999.
Number exceeding 999 will have the same number of commas , that of difference between n and 999.
Number below 999 will simply have output as 0

