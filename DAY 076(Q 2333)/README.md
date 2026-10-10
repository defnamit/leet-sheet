# **2333. Minimum Sum of Squared Difference**


You are given two positive 0-indexed integer arrays nums1 and nums2, both of length n.

The sum of squared difference of arrays nums1 and nums2 is defined as the sum of (nums1[i] - nums2[i])2 for each 0 <= i < n.

You are also given two positive integers k1 and k2. You can modify any of the elements of nums1 by +1 or -1 at most k1 times. Similarly, you can modify any of the elements of nums2 by +1 or -1 at most k2 times.

Return the minimum sum of squared difference after modifying array nums1 at most k1 times and modifying array nums2 at most k2 times.

Note: You are allowed to modify the array elements to become negative integers.

 


# MY EXPLANATION-


Let me tell you our approach in abstract way step by step.

Step 1) We must have to know the difference between the corresponding numbers and then calculate (k1+k2) to know that how many operations are we allowed to do.

(We are minimizing the difference because that will ultimately minimize the sum of square)

Step 2) Will use binary sort method to level the difference , because we want to remove the disparities among the difference and bring them to an average level.

(mid is used to find mid value between shortest and largest number , basically to find our between level, and need is telling us that how many operation is required for to reach that certain level)

Step 3) Remaining is used to find that , do we have remaining operations left after we bring every value to that level.

Step 4) min operator is used to bring down each element to that particular level or around that level , so no element can be exceeded to that average level.

Step 5) Now we will use that remaining operations , we will contract each level more to reduce our sum, we will iterate in the diff to find the numbers which are already leveled and reduce it.

(We are reducing only leveled difference because we already have difference in our list diff which are smaller than level , now we will use the rest of our operations to reduce the greatest numbers that are levels itself)

step 6) At last we will calculate the sum of all squares of difference , and that will be our minimum.

