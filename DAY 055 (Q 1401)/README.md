# **1401. Circle and Rectangle Overlapping**



You are given a circle represented as (radius, xCenter, yCenter) and an axis-aligned rectangle represented as (x1, y1, x2, y2), where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the rectangle.

Return true if the circle and rectangle are overlapped otherwise return false. In other words, check if there is any point (xi, yi) that belongs to the circle and the rectangle at the same time.
&#x20;



# MY EXPLANATION-



SO basically what i did in solution was that , found two points that is x and y.
x is nearest x axis distance from the centre and same goes with y variable too.


Understanding how x and y are taking values: min operator and max operator inside is actually checking that we dont go too far from the boundaries.

And at last we will use the Euclidean distance formula , to know that whether the nearest points(x,y) we found is inside the range of radius or not, if yes then only we can say that the two shapes are overlapping.