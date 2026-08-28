from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        half_len = n // 2
        freq = Counter(s)
        
        # Validate palindrome capability
        odd_chars = [c for c, count in freq.items() if count % 2 != 0]
        if (n % 2 == 0 and len(odd_chars) > 0) or (n % 2 != 0 and len(odd_chars) > 1):
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        if mid_char:
            freq[mid_char] -= 1
        
        # Half counts for the left side
        left_freq = {c: count // 2 for c, count in freq.items()}
        
        def build_smallest(available):
            return "".join(c * available[c] for c in sorted(available.keys()))
        
        # Helper to construct full string from half prefix and middle character
        def form_palindrome(left_str, remaining):
            tail = build_smallest(remaining)
            first_half = left_str + tail
            if n % 2 == 0:
                return first_half + first_half[::-1]
            return first_half + mid_char + first_half[::-1]

        best_res = None
        curr_left = []
        rem_freq = left_freq.copy()
        
        # Try matching prefixes of increasing length with target's prefix
        for i in range(half_len + 1):
            if i < half_len:
                t_char = target[i]
                for c in sorted(rem_freq.keys()):
                    if c > t_char and rem_freq[c] > 0:
                        rem_freq[c] -= 1
                        candidate = form_palindrome("".join(curr_left) + c, rem_freq)
                        if candidate > target:
                            if best_res is None or candidate < best_res:
                                best_res = candidate
                        rem_freq[c] += 1
                
                # Advance prefix match with target[i]
                if rem_freq.get(t_char, 0) > 0:
                    curr_left.append(t_char)
                    rem_freq[t_char] -= 1
                else:
                    break
            else:
                candidate = form_palindrome("".join(curr_left), rem_freq)
                if candidate > target:
                    if best_res is None or candidate < best_res:
                        best_res = candidate

        return best_res if best_res is not None else ""
