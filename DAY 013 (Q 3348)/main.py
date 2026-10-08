from collections import Counter

class Solution(object):
    def smallestNumber(self, num, t):
        num = str(num)

        # Prime factors required by t
        need = [0, 0, 0, 0]   # 2, 3, 5, 7
        primes = [2, 3, 5, 7]

        for i, p in enumerate(primes):
            while t % p == 0:
                need[i] += 1
                t //= p

        # If t has another prime factor, impossible
        if t > 1:
            return "-1"

        # Factor contribution of every digit
        factors = {
            1: [0, 0, 0, 0],
            2: [1, 0, 0, 0],
            3: [0, 1, 0, 0],
            4: [2, 0, 0, 0],
            5: [0, 0, 1, 0],
            6: [1, 1, 0, 0],
            7: [0, 0, 0, 1],
            8: [3, 0, 0, 0],
            9: [0, 2, 0, 0]
        }

        def enough(req, slots):
            """Can req be satisfied using at most slots digits?"""

            # 5 and 7 can only be supplied by 5 and 7
            if req[2] > slots or req[3] > slots:
                return False

            slots -= req[2] + req[3]

            # Use 9 for pairs of 3
            d9 = req[1] // 2
            req3 = req[1] % 2

            # Use 8 for groups of 3 twos
            d8 = req[0] // 3
            req2 = req[0] % 3

            # 6 can satisfy one 2 and one 3
            if req2 and req3:
                req2 = 0
                req3 = 0
                slots -= 1

            # 4 can satisfy two 2s
            d4 = req2 // 2
            req2 %= 2

            # Remaining 2 or 3 each need one digit
            needed = d9 + d8 + d4 + req2 + req3

            return needed <= slots

        def build(req, slots):
            """Build the smallest suffix satisfying req."""

            ans = []

            # We want the smallest number, so try digits 1 → 9
            for d in range(1, 10):
                f = factors[d]

                new_req = [
                    max(0, req[j] - f[j])
                    for j in range(4)
                ]

                if enough(new_req, slots - 1):
                    ans.append(str(d))
                    req = new_req
                    slots -= 1

                    if slots == 0:
                        break

                    # Continue filling remaining positions
                    while slots:
                        for x in range(1, 10):
                            fx = factors[x]
                            test = [
                                max(0, req[j] - fx[j])
                                for j in range(4)
                            ]

                            if enough(test, slots - 1):
                                ans.append(str(x))
                                req = test
                                slots -= 1
                                break

            return "".join(ans)

        # Check if num itself works
        current = [0, 0, 0, 0]

        if '0' not in num:
            for ch in num:
                f = factors[int(ch)]
                for j in range(4):
                    current[j] += f[j]

            if all(current[j] >= need[j] for j in range(4)):
                return num

        # Try making num slightly larger.
        # Start from the rightmost digit.
        for i in range(len(num) - 1, -1, -1):

            # Leading zero is not allowed
            start = int(num[i]) + 1

            for d in range(start, 10):

                if i == 0 and d == 0:
                    continue

                # Factor contribution of prefix
                req = need[:]

                for ch in num[:i]:
                    f = factors[int(ch)]
                    for j in range(4):
                        req[j] = max(0, req[j] - f[j])

                # Factor contribution of new digit
                f = factors[d]

                for j in range(4):
                    req[j] = max(0, req[j] - f[j])

                slots = len(num) - i - 1

                if enough(req, slots):
                    suffix = build(req, slots)
                    return num[:i] + str(d) + suffix

        # If no number of the same length works,
        # create the smallest number with one extra digit.
        suffix = build(need[:], len(num) + 1)

        return suffix
