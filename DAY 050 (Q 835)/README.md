# **835. Image Overlap**



You are given two images, img1 and img2, represented as binary, square matrices of size n x n. A binary matrix has only 0s and 1s as values.



We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the overlap by counting the number of positions that have a 1 in both images.



Note also that a translation does not include any kind of rotation. Any 1 bits that are translated outside of the matrix borders are erased.



Return the largest possible overlap.

# **MY EXPLANATION-**



This can have an easy approach but let me tell you my mistake i did so you can also learn from my mistakes,
what i did at first was , i wrote 4 different functions to shift the array up,down,left,right but after that too checking the conditions when to shift array up or down made it more tedious and increases the whole run time.

After analysing more in depth i realized our main priority is not just to shift the array , basically what we mainly want is the max number of overlapping 1's after shifting multiple times and this realization made me shorten my code, and now in this code the main basic idea is to know that at how many shifts we can gather more number of overlapping 1's.

So now lets talk about my code , we will be using numpy , because it will help us doing some of the operations easily.
argwhere() is numpy keyword , basically it will return list of indices where 1 exist in the whole array.
This r and c will tell us the distance between the two nearby 1's , so that we can know how many shifts will be needed to make a overlapping.

Main part , shifts\[(r, c)] = shifts.get((r, c), 0) + 1
We are basically storing in the dictionary total number of overlapping 1's we create after we shift certain number of positions, and at last using max we can get the highest number of overlapping 1 among all overlapping we created on certain shifts.

