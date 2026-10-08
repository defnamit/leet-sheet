# **1927. Sum Game**





**Alice and Bob take turns playing a game, with Alice starting first.**



**You are given a string num of even length consisting of digits and '?' characters. On each turn, a player will do the following if there is still at least one '?' in num:**



**Choose an index i where num\[i] == '?'.**

**Replace num\[i] with any digit between '0' and '9'.**

**The game ends when there are no more '?' characters in num.**



**For Bob to win, the sum of the digits in the first half of num must be equal to the sum of the digits in the second half. For Alice to win, the sums must not be equal.**



**For example, if the game ended with num = "243801", then Bob wins because 2+4+3 = 8+0+1. If the game ended with num = "243803", then Alice wins because 2+4+3 != 8+0+3.**

**Assuming Alice and Bob play optimally, return true if Alice will win and false if Bob will win.**



&#x20;



# ***MY EXPLANATION-***



We know that , the total number of digits in the integer is even .
If we get to know that number of question marks are odd , then the alice will have all the power to win the game , because she can end the game according to her own choice , and playing the last chance she can create an imbalancement , means she can win.

Else if question marks are even, we know the average of the number question mark can be replaced is (9/2= 4.5) , so if we know the impact difference created by the sum of numbers on both the side is equal or not to the difference of the question marks and the imapct of 4.5 it can create , we will get our answer

