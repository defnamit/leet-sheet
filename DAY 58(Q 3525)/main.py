class Node:
    def __init__(self, k: int):
        self.prod = 1
        self.cnt = [0] * k

class SegmentTree:
    def __init__(self, nums: list[int], k: int):
        self.n = len(nums)
        self.k = k
        self.tree = [Node(k) for _ in range(4 * self.n)]
        self._build(nums, 0, 0, self.n - 1)

    def _merge(self, left: Node, right: Node) -> Node:
        res = Node(self.k)
        res.prod = (left.prod * right.prod) % self.k

        # 1. Prefixes entirely contained within the left child
        for r in range(self.k):
            res.cnt[r] = left.cnt[r]

        # 2. Prefixes that cross into the right child
        for r in range(self.k):
            if right.cnt[r] > 0:
                target_r = (left.prod * r) % self.k
                res.cnt[target_r] += right.cnt[r]

        return res

    def _build(self, nums: list[int], node: int, l: int, r: int):
        if l == r:
            val = nums[l] % self.k
            self.tree[node].prod = val
            self.tree[node].cnt[val] = 1
            return

        mid = (l + r) // 2
        self._build(nums, 2 * node + 1, l, mid)
        self._build(nums, 2 * node + 2, mid + 1, r)
        self.tree[node] = self._merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def update(self, idx: int, val: int):
        def _update(node: int, l: int, r: int):
            if l == r:
                rem = val % self.k
                self.tree[node].prod = rem
                self.tree[node].cnt = [0] * self.k
                self.tree[node].cnt[rem] = 1
                return

            mid = (l + r) // 2
            if idx <= mid:
                _update(2 * node + 1, l, mid)
            else:
                _update(2 * node + 2, mid + 1, r)

            self.tree[node] = self._merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

        _update(0, 0, self.n - 1)

    def query(self, ql: int, qr: int) -> Node:
        def _query(node: int, l: int, r: int) -> Node:
            if ql <= l and r <= qr:
                return self.tree[node]

            mid = (l + r) // 2
            if qr <= mid:
                return _query(2 * node + 1, l, mid)
            if ql > mid:
                return _query(2 * node + 2, mid + 1, r)

            left_res = _query(2 * node + 1, l, mid)
            right_res = _query(2 * node + 2, mid + 1, r)
            return self._merge(left_res, right_res)

        return _query(0, 0, self.n - 1)


class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        st = SegmentTree(nums, k)
        ans = []
        n = len(nums)

        for idx, val, start, x in queries:
            # Step 1: Perform point update
            st.update(idx, val)

            # Step 2: Query the subarray range [start, n - 1]
            res_node = st.query(start, n - 1)

            # Step 3: Extract count of prefixes whose modulo matches x
            ans.append(res_node.cnt[x])

        return ans
