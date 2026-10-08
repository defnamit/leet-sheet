class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:

        def dfs(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                
                if expression[i] == '{':
                    inside, i = dfs(i + 1)

                elif expression[i].isalpha():
                    inside = {expression[i]}
                    i += 1

                elif expression[i] == ',':
                    result.update(current)
                    current = {""}
                    i += 1
                    continue

                # Concatenation
                current = {a + b for a in current for b in inside}

            result.update(current)

            return result, i + 1

        ans, _ = dfs(0)

        return sorted(ans)
