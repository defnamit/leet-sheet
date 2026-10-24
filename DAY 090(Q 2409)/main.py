class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:

        d = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def convert(date):
            month = int(date[0:2])
            day = int(date[3:5])

            return sum(d[1:month]) + day

        alice_start = convert(arriveAlice)
        alice_end = convert(leaveAlice)

        bob_start = convert(arriveBob)
        bob_end = convert(leaveBob)

        start = max(alice_start, bob_start)
        end = min(alice_end, bob_end)

        return max(0, end - start + 1)
