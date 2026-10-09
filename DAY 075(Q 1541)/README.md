# **1541. Minimum Insertions to Balance a Parentheses String**


Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:

Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.

For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
You can insert the characters '(' and ')' at any position of the string to balance it if needed.

Return the minimum number of insertions needed to make s balanced.



# MY EXPLANATION-


1. `ans = 0` counts the number of brackets inserted, and `need = 0` tracks required closing brackets `)`.

2. Every `(` requires two consecutive `)` to balance it, so we increase `need` by 2.

3. If `need % 2 == 1`, we insert one `)` to finish the previous requirement before processing a new `(`.

4. `ans += 1` counts that inserted closing bracket.

5. `need -= 1` accounts for the inserted bracket, and `need += 2` creates the requirement for the new `(`.

6. When we encounter `)`, we decrease `need` by 1 because one required closing bracket is satisfied.

7. If `need < 0`, we have an extra `)` without an opening bracket, so we insert `(` and increase `ans`.

8. We set `need = 1` because the newly inserted `(` still needs two `)`, and the current `)` satisfies one of them.

9. After processing the string, any remaining `need` represents missing closing brackets.

10. Therefore, we return `ans + need` to get the minimum total insertions.
