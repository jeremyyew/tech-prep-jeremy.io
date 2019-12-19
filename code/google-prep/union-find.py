

def testUF(find, union, connected):
    def contains_cycle(g):
        # Where g is an adj list.
        arr = list(range(len(g)))
        for u in range(len(g)):
            for v in g[u]:
                if connected(arr, u, v):
                    return True
                union(arr, u, v)
        return False

    def process_adjacency_list(arr, g):
        for u in range(len(g)):
            for v in g[u]:
                union(arr, u, v)

    def process_adjacency_matrix(arr, g):
        for u in range(len(g)):
            for v in range(len(g[u])):
                if g[u][v]:
                    union(arr, u, v)

    def asserts(arr):
        assert(connected(arr, 0, 1))
        assert(connected(arr, 1, 2))
        assert(connected(arr, 2, 0))
        assert(connected(arr, 0, 2))
        assert(not connected(arr, 0, 3))

    arr = list(range(4))
    union(arr, 0, 1)
    union(arr, 1, 2)
    union(arr, 2, 0)
    asserts(arr)

    arr = list(range(4))
    g1 = [[1, 2], [2], [], []]
    assert(contains_cycle(g1))
    process_adjacency_list(arr, g1)
    asserts(arr)

    arr = list(range(4))
    g2 = [[False, True, True, False],
          [False, False, True, False],
          [False, False, False, False],
          [False, False, False, False]]
    process_adjacency_matrix(arr, g2)
    asserts(arr)

# UNION FIND QUICK.


def find(arr, u):  # O(1).
    return arr[u]


def union(arr, u, v):  # Exactly N.
    if arr[u] == arr[v]:
        return
    parent_u = arr[u]
    for i in range(len(arr)):
        if arr[i] == parent_u:
            arr[i] = arr[v]


def connected(arr, u, v):  # O(1).
    return find(arr, u) == find(arr, v)


testUF(find, union, connected)
print(f"Union Find Quick passed tests.")


# UNION FIND TREE W PATH COMPRESSION. With a tree of pointers and path compression.
# The main benefit is that for unions, we only write to one value (the root of one component), and we only traverse the path, which is often less than N. The added cost to find and connected can be mitigated by path compression, which will also help union.

def find(arr, u):
    if arr[u] != u:
        arr[u] = find(arr, arr[u])
    return arr[u]


def connected(arr, u, v):
    return find(arr, u) == find(arr, v)


def union(arr, u, v):
    root_u, root_v = find(arr, u), find(arr, v)
    arr[root_u] = root_v


testUF(find, union, connected)
print(f"Union Find Tree w path compression passed tests.")
