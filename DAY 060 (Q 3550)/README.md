# **3550. Smallest Index With Digit Sum Equal to Index**



You are given an integer array nums.

Return the smallest index i such that the sum of the digits of nums[i] is equal to i.

If no such index exists, return -1.


# MY EXPLANATION-



Eazzz , i know what complicated part you saw in my code , let me make easy for you.

So we will obviously run a if loop and,


sum(list(map(int,str(nums[i]))))) so we are using a map function , basically map function is applied to that data type where we want to perform same operation on that whole data type,
Just like here we are basically converting the single int value to the list were every of the position of int (like tens , hundreds etc) are written seperately .


In the map function , we provide first argument as int in which we want our data type to be and We write str(num) because the map() function requires an iterable (like a string, list, or tuple) as its second argument.


Simply using sum operation we will find our smallest index , THATS ITTTTT.