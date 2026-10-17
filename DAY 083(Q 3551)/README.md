# **3551. Minimum Swaps to Sort by Digit Sum**


You are given an array nums of distinct positive integers. You need to sort the array in increasing order based on the sum of the digits of each number. If two numbers have the same digit sum, the smaller number appears first in the sorted order.

Return the minimum number of swaps required to rearrange nums into this sorted order.

A swap is defined as exchanging the values at two distinct positions in the array.




# MY EXPLANATION-


Learned something crazzzy today , let me teach you too , lesgooo.

What are we doing in this question ----

1) We will be creating a new list (l) , using for loop , we will calculate the sum for each number , and we will be using the same old technique of map.
Also we will store the sum , its index , number itself in the list as a form of tuple , because these 3 info are very important so we will store them as a history.


2) Using sorted and key method we will sort the element , the thing written inside lambda of key is , x[0] means we will primarily sort using sum (sum is stored at the 0 index of tuple ) , and if the sum gets equal we will then sort on the basis of x[2] (number is stored at the 2 index) as given in the question itself.



3) We will be using a cycle loop method (its not the original name i just wrote it's name for fun)


4) In this method basically , we will be cycling like a loop in the array , and also keep track of the indexes / element we visited earlier .

(Basically we will see that is the sorted element still in its place or it just deviated , if it is deviated we will just reach at its past location , and the element present there is also deviated we will again reach its past location , and we will continue to do so , until we reach at any true place or position we visited earlier).


This creates a loop cycle of a fixed length , and if you wanna know how many swaps were made to sort this using the cycle length is swap=cycle_len -1 


Why -1? Because in every cycle loop , we travel n times to reach at a particular location we already visited , so why to count that location 2 times , that is why we do n-1 , (n is the total steps , and -1 for the same location we are visiting twice to end our loop)


And that's it , if you properly look our code , you will understand what i am trying to say , what does if in the loop means and so on.


I hope you understood , dhanywaad mittar. 

