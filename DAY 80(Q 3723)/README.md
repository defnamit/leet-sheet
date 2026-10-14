# **3723. Maximize Sum of Squares of Digits**


You are given two positive integers num and sum.

A positive integer n is good if it satisfies both of the following:

The number of digits in n is exactly num.
The sum of digits in n is exactly sum.
The score of a good integer n is the sum of the squares of digits in n.

Return a string denoting the good integer n that achieves the maximum score. If there are multiple possible integers, return the maximum ​​​​​​​one. If no such integer exists, return an empty string. 


# MY EXPLANATION-


Our main aim here will be to find the greatest good integer , its squares will be automatically the bigger one.

We will treat each digit of an integer separately , that is why we have created a list of zeroes , length equal to num (as mentioned in the question ), and variable i to secure positions in the list l.


So now listen my abstract idea , we will run a while loop until the sum becomes 0 , because we will decrease the sum loop by loop according to the situation.


So our main aim is to create a number whose sum equals to "sum" , the largest number we can have at a place in any integer is 9 , and that will happen when the sum we can to achieve is bigger than 9 , (lets suppose it is 15 , we cant reach till 15 directly , as it is bigger than 9 , we have to cross the bridge of 9 first then if it is needed to cross one more 9 bridge we will , but here after 9 we can just simple reach 6 to get 15 after adding both).


And as soon we reach our bridges , we will decrease that many value from the sum .

Notice what first if case is indicating , there can be scenario if the list gets filled with 9 but still we can get our sum , that is an invalid case so will return "".


At last we will collapse the elements of list , to create one numeric string.