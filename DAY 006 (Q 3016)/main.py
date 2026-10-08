from collections import Counter

class Solution(object):
    def minimumPushes(self, word):
        count = Counter(word)
        freq = sorted(count.values(), reverse=True)

        total = 0

        for i, f in enumerate(freq):
            pushes = i // 8 + 1
            total += pushes * f

        return total
