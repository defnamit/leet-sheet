class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:

        first = {}
        last = {}

        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        intervals = []

        for ch in first:
            l = first[ch]
            r = last[ch]

            i = l
            valid = True

            while i <= r:
                c = s[i]

                if first[c] < l:
                    valid = False
                    break

                r = max(r, last[c])
                i += 1

            if valid:
                intervals.append((l, r))

        intervals.sort(key=lambda x: x[1])

        ans = []
        prev_end = -1

        for l, r in intervals:
            if l > prev_end:
                ans.append(s[l:r + 1])
                prev_end = r

        return ans
