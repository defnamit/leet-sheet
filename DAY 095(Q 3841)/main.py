class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        i += 1
        while i <= self.n:
            self.tree[i] ^= delta
            i += i & -i

    def query(self, i):
        res = 0
        while i:
            res ^= self.tree[i]
            i -= i & -i
        return res


class Solution:
    def palindromePath(self, n, edges, s, queries):
        import sys
        sys.setrecursionlimit(100000)

        g = [[] for _ in range(n)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        def dfs(u, p):
            nonlocal timer

            parent[u] = p
            tin[u] = timer
            timer += 1

            for v in g[u]:
                if v != p:
                    depth[v] = depth[u] + 1
                    dfs(v, u)

            tout[u] = timer

        dfs(0, -1)

        m = n.bit_length()
        up = [parent[:]]
        up[0][0] = 0

        for j in range(1, m):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            d = depth[u] - depth[v]
            j = 0

            while d:
                if d & 1:
                    u = up[j][u]
                d >>= 1
                j += 1

            if u == v:
                return u

            for j in range(m - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return parent[u]

        bits = [1 << (ord(c) - ord('a')) for c in s]

        bit = BinaryIndexedTree(n)

        for u in range(n):
            bit.update(tin[u], bits[u])
            bit.update(tout[u], bits[u])

        ans = []

        for q in queries:
            op, a, b = q.split()
            u = int(a)

            if op == "update":
                new_bit = 1 << (ord(b) - ord('a'))
                delta = bits[u] ^ new_bit

                if delta:
                    bit.update(tin[u], delta)
                    bit.update(tout[u], delta)
                    bits[u] = new_bit

            else:
                v = int(b)
                w = lca(u, v)

                mask = (
                    bit.query(tin[u] + 1)
                    ^ bit.query(tin[v] + 1)
                    ^ bits[w]
                )

                ans.append((mask & (mask - 1)) == 0)

        return ans
