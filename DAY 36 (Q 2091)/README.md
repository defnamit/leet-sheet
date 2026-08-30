# **2091. Removing Minimum and Maximum From Array**





**You are given a 0-indexed array of distinct integers nums.**



**There is an element in nums that has the lowest value and an element that has the highest value. We call them the minimum and maximum respectively. Your goal is to remove both these elements from the array.**



**A deletion is defined as either removing an element from the front of the array or removing an element from the back of the array.**



**Return the minimum number of deletions it would take to remove both the minimum and maximum element from the array.**



# **MY EXPLANATION-**





**First approach will always be to know the position or indices of the minimum and maximum numbers in the array.
As to draw our cases we compulsorily need to know that which number is closer from the start of the array and which is closer from the last and that is what our if condition is doing.
Talking about cases , we will have 3 major cases that can be concluded to have an appropriate output.


CASE 1 = The both numbers would be near from the start and the back of the array
CASE 2 = Both the numbers would be near from the start of the array**
CASE 3 = Both the numbers would be near from the end of the array.

Using min operator and determining which case will have minimum number of deletion , we will solve this ques.**

