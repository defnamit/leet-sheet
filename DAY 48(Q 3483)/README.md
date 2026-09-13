# **3483. Unique 3-Digit Even Numbers**



You are given an array of digits called digits. Your task is to determine the number of distinct three-digit even numbers that can be formed using these digits.



Note: Each copy of a digit can only be used once per number, and there may not be leading zeros. 



# **MY EXPLANATION-**



This is not the best approach , but for the easy question you can consider it .
So basically what brute force approach is we will going to run three loops , each for ones, tens and hundreds.


First condition, because we dont want repetitive numbers , thats what we are checking that if the indices overlap of any of them we will skip the current iteration.

Second condition, we actually dont want 0 at our hundreds place because eventually it will make the whole digit as a two digit number only , and we want three.

Third condition , the most important thing to check if the number is even or not , and if the ones place is even then the whole number is even only.

At last we will combine that using basic maths (hundreds + tens + ones)

If you wondering why we created set , so we dont want the duplicate numbers , and set will help us to reduce redundancy.


