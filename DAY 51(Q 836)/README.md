# **836. Rectangle Overlap**



An axis-aligned rectangle is represented as a list \[x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.



Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.



Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.





# **MY EXPLANATION-**



1\. Each rectangle is represented as `\[x1, y1, x2, y2]`, where `(x1,y1)` is bottom-left and `(x2,y2)` is top-right.

2\. To overlap, the rectangles must overlap in \*\*both X and Y directions\*\*.

3\. The overlapping width is `min(x2) - max(x1)`.

4\. The overlapping height is `min(y2) - max(y1)`.

5\. If both `width > 0` and `height > 0`, the rectangles have positive overlapping area.

6\. Therefore, return `width > 0 and height > 0`.



