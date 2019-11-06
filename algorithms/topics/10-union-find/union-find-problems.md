# Union Find Problems

```python

from collections import defaultdict, Counter
import math


class UnionFindTreeWithPathCompression():
    # The main benefit is that for unions, we only write to one value (the root of one component), and we only traverse the path, which is often less than N. The added cost to find and connected can be mitigated by path compression, which will also help union.
    def __init__(self, num_nodes):
        self.components = list(range(num_nodes))

    def find(self, u):  # O(N), amortized O(1) with path compression.
        # Every time we find the root, we also recursively set all children to directly link to root node.
        # This incurs a one-time cost of path length of O(N), but future find calls will be O(1).
        if u != self.components[u]:
            root = self.find(self.components[u])
            self.components[u] = root
        return self.components[u]

    # O(path_length), which in worst case would be O(N). On average (across different nodes in all paths) this will be less than N.  Amortized O(1) with path compression.
    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)
        if root_u != root_v:
            self.components[root_u] = root_v

    def connected(self, u, v):  # O(N), amortized O(1) with path compression.
        return self.find(u) == self.find(v)

    def contains_cycle(self, g):
        # Takes g as adj list.
        # In order to have this behaviour work separate from the current state (but not make all our methods static or refactor all methods to take the component state), we save components and restore it later.
        temp = self.components
        # Assume our adj list has all nodes as keys - otherwise we shd get all unique elements.
        self.components = list(range(len(g.keys())))
        for u in g:
            for v in g[u]:
                if self.connected(u, v):
                    return True
                self.union(u, v)
        self.components = temp
        return False

    def process_adjacency_matrix(self, g):
        # Where edges are given any value that coerces to True.
        for u in range(len(g)):
            for v in range(len(g[u])):
                if g[u][v]:
                    self.union(u, v)

    def process_adjacency_list(self, g):
        # Where g is a dictionary with lists of neighbors.
        for u in g:
            for v in g[u]:
                self.union(u, v)


class UnionFindQuick():
    def __init__(self, num_nodes):
        # All nodes
        self.components = list(range(num_nodes))

    def find(self, u):  # O(1).
        return self.components[u]

    def union(self, u, v):  # Exactly N.
        if self.components[u] == self.components[v]:
            return
        self.components = [self.components[v] if e ==
                           self.components[u] else e for e in self.components]

    def connected(self, i, j):  # O(1).
        return self.find(i) == self.find(j)

    def process_adjacency_matrix(self, g):
        # Where edges are given any value that coerces to True.
        for u in range(len(g)):
            for v in range(len(g[u])):
                if g[u][v]:
                    self.union(u, v)

    def process_adjacency_list(self, g):
        # Where g is a dictionary with lists of neighbors.
        for u in g:
            for v in g[u]:
                self.union(u, v)

    def contains_cycle(self, g):
        # Same as UnionFindTreeWithPathCompression.
        temp = self.components
        self.components = list(range(len(g.keys())))
        for u in g:
            for v in g[u]:
                if self.connected(u, v):
                    return True
                self.union(u, v)
        self.components = temp
        return False


class LargestComponentSizeByCommonFactor(object):

    # https://leetcode.com/problems/largest-component-size-by-common-factor/
    def largestComponentSize(self, A):
        uf = UnionFindTreeWithPathCompression(max(A)+1)
        # Very inefficient to store all factors as individual components, but necessary since our implementation uses a list.
        # Let us implement a dictionary version. Check out https://leetcode.com/problems/largest-component-size-by-common-factor/discuss/261572/Straight-forward-python-solution.
        for num in A:
            for i in range(2, int(math.sqrt(num)+1)):
                if num % i == 0:
                    uf.union(num, i)
                    uf.union(num, num//i)
        parents = [uf.find(num) for num in A]
        return max(Counter(parents).values())


test_cases = (([4, 6, 15, 35], 4),
              ([20, 50, 9, 63], 2),
              ([2, 3, 6, 7, 4, 12, 21, 39], 8))
for l, r in test_cases:
    assert(LargestComponentSizeByCommonFactor().largestComponentSize(l) == r)
print("LargestComponentSizeByCommonFactor with UnionFindTreeWithPathCompression passed test.")


class AccountsMerge(object):
    # https://leetcode.com/problems/accounts-merge/
    def accountsMerge(self, accounts):
        # Group accounts with same names together.
        email_lists_by_name = defaultdict(list)
        for acc_list in accounts:
            email_lists_by_name[acc_list[0]].append(acc_list[1:])

        res = []
        for name, email_lists in email_lists_by_name.items():
            map_by_index = list(set([el for els in email_lists for el in els]))
            map_by_email = {e: i for i, e in enumerate(map_by_index)}
            uf = UnionFindTreeWithPathCompression(len(map_by_index))
            for el in email_lists:
                for i in range(1, len(el)):
                    uf.union(map_by_email[el[0]], map_by_email[el[i]])
            partition = defaultdict(list)
            for i, v in enumerate(uf.components):
                root = uf.find(v)
                partition[root].append(i)
            for component in partition.values():
                res.append([name] + sorted([map_by_index[c]
                                            for c in component]))
        return res


accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], [
    "John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
result = [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  [
    "John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]

assert(sorted(AccountsMerge().accountsMerge(accounts)) == result)
# Definitely use tree approach w path compression here, there are lots of finds on big sets. Otherwise UFQuick will exceed timelimit.
print("AccountsMerge with UnionFindTreeWithPathCompression passed test.")
# assert(sorted(Solution().accountsMerge(accounts)) == result)
# print("accountsMerge with UnionFindQuick passed test.")


class FriendCircles(object):
    # https://leetcode.com/problems/friend-circles/s
    def findCircleNum(self, M):
        uf = UnionFindQuick(len(M))
        uf.process_adjacency_matrix(M)
        num_components = len(
            list([v for i, v in enumerate(uf.components) if i == v]))
        return num_components


m1 = [[1, 1, 0],
      [1, 1, 0],
      [0, 0, 1]]

m2 = [[1, 1, 0],
      [1, 1, 1],
      [0, 1, 1]]

assert(FriendCircles().findCircleNum(m1) == 2)
assert(FriendCircles().findCircleNum(m2) == 1)
print("FriendsCircles with UnionFindQuick passed tests.")


# https://leetcode.com/problems/satisfiability-of-equality-equations/


def test_uf(uf_candidate):

    def run_asserts(uf):
        assert(uf.connected(0, 1))
        assert(uf.connected(1, 2))
        assert(uf.connected(2, 0))
        assert(uf.connected(0, 2))
        assert(not uf.connected(0, 3))

    uf = uf_candidate(4)
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(2, 0)
    run_asserts(uf)

    uf = uf_candidate(4)
    g1 = {0: [1, 2], 1: [2], 2: [], 3: []}
    uf.process_adjacency_list(g1)
    run_asserts(uf)
    assert(uf.contains_cycle(g1))

    uf = uf_candidate(4)
    g2 = [[False, True, True, False],
          [False, False, True, False],
          [False, False, False, False],
          [False, False, False, False]]
    uf.process_adjacency_matrix(g2)
    run_asserts(uf)

    print(f"Implementation {uf.__class__.__name__} passed tests.")


test_uf(UnionFindQuick)
test_uf(UnionFindTreeWithPathCompression)

```

