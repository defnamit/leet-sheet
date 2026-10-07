from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        def isValid(string):
            count = 0

            for ch in string:
                if ch == '(':
                    count += 1

                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        queue = deque([s])
        visited = {s}
        answer = []

        while queue:

            # Process one complete level
            for _ in range(len(queue)):

                curr = queue.popleft()

                # If valid, this is the minimum-removal level
                if isValid(curr):
                    answer.append(curr)

                # Generate next level only if no answer found yet
                if not answer:
                    for i in range(len(curr)):

                        # Only remove parentheses
                        if curr[i] not in "()":
                            continue

                        new_string = curr[:i] + curr[i + 1:]

                        if new_string not in visited:
                            visited.add(new_string)
                            queue.append(new_string)

            # Once valid strings are found, don't go to deeper levels
            if answer:
                break

        return answer

