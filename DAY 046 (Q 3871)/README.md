# **3871. Count Commas in Range II**



You are given an integer n.

Return the total number of commas used when writing all integers from [1, n] (inclusive) in standard number formatting.

In standard formatting:

A comma is inserted after every three digits from the right.
Numbers with fewer than 4 digits contain no commas.


# MY EXPLANATION-


Here we will start from the shortest number from which we start putting commas , that is obviously 1000.

Will run while loop until 1000 gets bigger than n , if n is smaller than 1000 , that means no comma can be placed , and 0 will be returned.


Inside the loop , end is used to fetch the value between the range of 1000 to 999999 (for first iteration) , because 999999 is the highest number that can contain only one comma , and initially we want to count the numbers with one comma only thats why we chose 999999 , and as the iteration continues start value increases and so our conditions for end.


Now count will be used to calculate the numbers that is present with suitable number of commas between the range from start, and in the final ans we need number with that suitable number of commas only , that is why we will multiple count of all such numbers with the comma.


Now we will make our start jump to another place which will contain 2 commas that is 1000000 (because A comma is inserted after every three digits from the right) , and meanwhile we will increase our number of comma by +1.

And the loop will iterate until we reach the n .