# **1477. Find Two Non-overlapping Sub-arrays Each With Target Sum**





You are given an array of integers arr and an integer target.

You have to find two non-overlapping sub-arrays of arr each with a sum equal target. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.

Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.

&#x20;



# MY EXPLANATION-



We will be using two pointer in the array , one is left and right pointer.
Total is here to calculate sum of the subarrays.
Best array is used so we can know the smallest subarray found till that index.
Shortest will store the shortest length of the subarray found till now , and ans will store the actual answer.
We have initialized these 3 at infinite , because we are performing min operation on them .

We will iterate the right pointer , and move left pointer as well with respect to the target value.
When we will encounter total = target , we will immediately store its length , and if we have two values by far then only if left > 0 and best[left - 1] != INF: this loop will run .
This loop will basically store the value of minimum length subarray , here best[left-1] will be telling us the previous length of the valid subarray.
And in the shortest we will be storing the shortest length of the valid subarray, as well as in the best array to with index=right.

And finally we will return our answer only if its not infinite(no valid subarray found)

