# **540. Single Element in a Sorted Array**


You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.


# MY EXPLANATION-



This question was asked in the DSA round of Zomato. I got to know about it from Reels too. Let's dive into the question.

If you look at what the question is asking, you will know that there is an array containing several numbers, including several repeated numbers, and you have to find the one specific number which is not repeated. It's not that tough a question. You can solve it in various ways but if you look at the question, it clearly states that the time complexity for your solution should be log n and the space complexity should be 1.

If you keep this in mind then you will know that the time complexity of the binary search method is log n and using binary search you could easily solve this question. How? Let's take a look.

The main thing which I am going to tell you is the whole base thing of this question. If you know this you could easily solve the question. If the array is sorted and every number is repeated, you will notice one pattern: the first number of the repeated pair will always lie on an even index and the second number of that repeated pair will always lie on an odd index. That's the whole basic thing.

