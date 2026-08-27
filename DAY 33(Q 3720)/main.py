from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)
        
        # Step 1: Find the maximum matching prefix length using available characters
        matched_len = 0
        while matched_len < n and counts[target[matched_len]] > 0:
            counts[target[matched_len]] -= 1
            matched_len += 1
            
        # Step 2: Try to find the divergence point from matched_len down to 0
        for k in range(matched_len, -1, -1):
            if k < n:
                # Find the smallest available character > target[k]
                target_char = target[k]
                for char_code in range(ord(target_char) + 1, ord('z') + 1):
                    ch = chr(char_code)
                    if counts[ch] > 0:
                        # Construct the solution: prefix + ch + remaining sorted chars
                        prefix = target[:k]
                        
                        # Use character 'ch' at index k
                        counts[ch] -= 1
                        
                        # Collect remaining characters in ascending order
                        suffix = []
                        for code in range(ord('a'), ord('z') + 1):
                            c = chr(code)
                            suffix.append(c * counts[c])
                        
                        return prefix + ch + "".join(suffix)
            
            # Backtrack: add target[k - 1] back to frequency counts for the next iteration
            if k > 0:
                counts[target[k - 1]] += 1
                
        return ""
