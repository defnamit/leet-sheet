# **2948. Make Lexicographically Smallest Array by Swapping Elements**





**You are given a 0-indexed array of positive integers nums and a positive integer limit.**



**In one operation, you can choose any two indices i and j and swap nums\[i] and nums\[j] if |nums\[i] - nums\[j]| <= limit.**



**Return the lexicographically smallest array that can be obtained by performing the operation any number of times.**



**An array a is lexicographically smaller than an array b if in the first position where a and b differ, array a has an element that is less than the corresponding element in b. For example, the array \[2,10,3] is lexicographically smaller than the array \[10,2,3] because they differ at index 0 and 2 < 10.**





# **MY EXPLANATION-**





**Our main aim here is not only to find swapable indices but also the whole group that mutually can be swapped in the given condition.
For that we will first be storing all elements of the array in another temp array called "arr" , and storage will be such that it stores both the element and the original index of that particular element.
We will be sorting arr, why? Becuase our main aim is to find lexicographic numbers , that is why after storing the number we will be forming groups using i and j in for loops , consecutive numbers will be then formed such as , smaller index will be assigned to the smallest number , and thats what lexicographic means .
And that is what we will be doing with all the groups we will form , and hence we will get our desired output.**

