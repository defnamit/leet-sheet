import numpy as np

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        img1 = np.array(img1)
        img2 = np.array(img2)

        if not (np.any(img1 == 1) and np.any(img2 == 1)):
            return 0

        l1 = np.argwhere(img1 == 1)
        l2 = np.argwhere(img2 == 1)

        shifts = {}

        for r1, c1 in l1:
            for r2, c2 in l2:

                r = r2 - r1
                c = c2 - c1

                shifts[(r, c)] = shifts.get((r, c), 0) + 1

        return max(shifts.values())
