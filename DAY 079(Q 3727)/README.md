# **3727. Maximum Alternating Sum of Squares**


You are given an integer array nums. You may rearrange the elements in any order.

The alternating score of an array arr is defined as:

score = arr[0]2 - arr[1]2 + arr[2]2 - arr[3]2 + ...
Return an integer denoting the maximum possible alternating score of nums after rearranging its elements.



# MY EXPLANATION-

If you analyze closely , you will get to know that all max elements are getting added and all min elements are getting subtracted , so our abstract approach will be to sort the array on the basis of square of elements. 


(key=lambda x: x * x) , key is a parameter which gives instruction , lambda acts as a function that instructs the key on what basis to sort.

Then we will get the middle point of the array , because logically if we sort an array in ascending order , then left side from middle are all the min values and right sides are the max value.

Min and max , thats what we needed and so basically we will use sum operator to calculate all the squares for both small and large elements .


At last by subtracting the large and small , we will get the answer.
