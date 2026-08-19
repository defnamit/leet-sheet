class Solution(object):
    def maxNumberOfFamilies(self, n, rs):

        reserved = {}

        for row, seat in rs:
            if row not in reserved:
                reserved[row] = set()
            reserved[row].add(seat)

        total = 2 * (n - len(reserved))

        for row in reserved:
            seats = reserved[row]

            left = all(x not in seats for x in range(2, 6))
            middle = all(x not in seats for x in range(4, 8))
            right = all(x not in seats for x in range(6, 10))

            if left and right:
                total += 2
            elif left or middle or right:
                total += 1

        return total
