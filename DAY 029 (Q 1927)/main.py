class Solution(object):
    def sumGame(self, num):

        n = len(num)
        half = n // 2
        
        sum1 = sum(int(c) for c in num[:half] if c != '?')
        sum2 = sum(int(c) for c in num[half:] if c != '?')
        
        q1 = num[:half].count('?')
        q2 = num[half:].count('?')
        
        if (q1 + q2) % 2 != 0:
            return True
        
        return (sum1 - sum2)  != (q2 - q1) * 4.5
