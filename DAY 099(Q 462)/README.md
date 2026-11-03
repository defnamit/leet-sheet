# **462. Minimum Moves to Equal Array Elements II**



Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.

Test cases are designed so that the answer will fit in a 32-bit integer.




# MY EXPLANATION-


Here we are allowed to increase or decrease by 1 , that too one by one.

The main part here is to choose the target value , target value is what you have to keep in mind to balance the array.

Here, if we take the median value as the target then the steps will be minimum (the number below the medium can be increased , the number above the median can be decreased, so it is the best target)


To find the median value , we will sort the array in ascending order and then find the median index (n//2) , through that index we can get the median value.

Then we will run the for loop , and find the difference between the median and current , using abs (it acts as mod function , it returns +ve value) .

Then we will return count.