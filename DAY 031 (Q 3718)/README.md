# **3718. Smallest Missing Multiple of K**





**Given an integer array nums and an integer k, return the smallest positive multiple of k that is missing from nums.**



**A multiple of k is any positive integer divisible by k.


MY EXPLANATION-**
---





**We will remove the duplicated number , because we dont need them , they will uselessly increase runtime.
Using set() will help us.
We will run a while loop , and find multiples of k , as soon as we dont get that particular multiple , we will return that number , and hence we will get our output**

