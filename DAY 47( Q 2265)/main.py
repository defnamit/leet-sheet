class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        ans = 0

        def dfs(root):
            nonlocal ans

            if root is None:
                return 0, 0

            left_sum, left_count = dfs(root.left)
            right_sum, right_count = dfs(root.right)

            total_sum = root.val + left_sum + right_sum
            total_count = 1 + left_count + right_count

            average = total_sum // total_count

            if root.val == average:
                ans += 1

            return total_sum, total_count

        dfs(root)

        return ans
