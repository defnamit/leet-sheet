class Solution:
    def totalNumbers(self, digits: list[int]) -> int:

        ans = set()

        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):

                    if i == j or i == k or j == k:
                        continue

                    if digits[i] == 0:
                        continue

                    if digits[k] % 2 != 0:
                        continue

                    num = digits[i] * 100 + digits[j] * 10 + digits[k]

                    ans.add(num)

        return len(ans)
