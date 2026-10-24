# **2409. Count Days Spent Together**


Alice and Bob are traveling to Rome for separate business meetings.

You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city from the dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the dates arriveBob to leaveBob (inclusive). Each will be a 5-character string in the format "MM-DD", corresponding to the month and day of the date.

Return the total number of days that Alice and Bob are in Rome together.

You can assume that all dates occur in the same calendar year, which is not a leap year. Note that the number of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].


# MY EXPLANATION-


This easy ques uses some part of your brain , but here we go again.


We have created a list , basically also given in the ques , with total number of days of each month , will be easy to directly retrieve from the list in further calculations.

Know what this convert function is doing , this picks up the date (in MM-DD format) , and converts that date accordingly to the nth day of a calendar , (for eg - 1 February = 32nd day of a year).

Now if you look at the function , you will know what we are doing , extracting the month and date while typecasting it into int , then summing the days for all months while slicing it from the above list + the residual days of the current month.


Comes the little main part , we will be finding max dates for the start of both alice and bob (because we want an overlap , and overlap occurs when b lies in the range of a).

End is calculated for both the person's trip , min is used because we want to ensure overlap condition , and for that we need the date which lies in any of the range (lying in the range also means shorter than the largest boundary).

Now return will finaly calculate the total days overlapped , end - start (calculates the actual overlap of days, and in valid situations end will be always greater than start) with +1 is used because we have to include the boundary dates too (as mentioned in ques).

If the start > end (cant be possible , if someone's starting a trip after other's trip is ended ) , will have a negative value , and eventually return 0.
