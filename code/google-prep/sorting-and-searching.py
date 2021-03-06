import unittest


class TestSort(unittest.TestCase):
    def test_quicksort(self):
        case1 = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5, 0]
        result1 = list(sorted(case1))

        case2 = [9, 1, 9, 1, 8, 3, 7, 4, 6, 5, 0]
        result2 = list(sorted(case2))

        quicksort(case1)
        self.assertEqual(case1, result1)
        quicksort(case2)
        self.assertEqual(case2, result2)

    def test_mergesort(self):
        case1 = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5, 0]
        result1 = list(sorted(case1))
        case2 = [9, 1, 9, 1, 8, 3, 7, 4, 6, 5, 0]
        result2 = list(sorted(case2))

        mergesort(case1)
        self.assertEqual(case1, result1)
        mergesort(case2)
        self.assertEqual(case2, result2)


def mergesort(arr):
    temp = [None for _ in range(len(arr))]

    def sort(l, r):  # l-inclusive, r-exclusive.
        if r - l < 2:
            return
        m = (l + r) // 2
        sort(l, m)
        sort(m, r)
        merge(l, m, r)

    def merge(l, m, r):
        # LHS: (l-inclusive, m-exclusive).  # RHS: (m-inclusive, r-exclusive).
        temp[l:r] = arr[l:r]

        curr = a = l
        b = m
        while a < m and b < r:
            if temp[a] <= temp[b]:
                arr[curr] = temp[a]
                a += 1
            else:
                arr[curr] = temp[b]
                b += 1
            curr += 1

        rem = m - a
        arr[curr:curr+rem] = temp[a:a+rem]

    sort(0, len(arr))


def quicksort(arr):
    def partition(l, r):  # l and r inclusive.
        pivot = arr[r]     # pivot
        for i in range(l, r):
            if arr[i] < pivot:
                arr[l], arr[i] = arr[i], arr[l]
                l += 1
        arr[l], arr[r] = arr[r], arr[l]
        return l

    def search(l, r):  # l and r inclusive.
        if l >= r:
            return
        pi = partition(l, r)
        search(l, pi-1)
        search(pi+1, r)

    search(0, len(arr) - 1)


class TestBinarySearch(unittest.TestCase):
    def test_BinarySearchIterative(self):
        result1 = 42
        case1 = [i for i in range(100)]

        self.assertEqual(binary_search(case1, 42), result1)
        self.assertIsNone(binary_search(case1, 200))


def binary_search(nums, k):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == k:
            return k
        elif nums[m] > k:
            r = m - 1
        else:
            l = m + 1
    return None


class TestSearchFirstLast(unittest.TestCase):
    def test_search_first_last(self):
        case1 = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(search_first_last(case1, 4), [3, 5])
        self.assertEqual(search_first_last(case1, 1), [0, 0])
        self.assertEqual(search_first_last(case1, 10), [11, 11])
        self.assertEqual(search_first_last(case1, 0), [-1, -1])
        self.assertEqual(search_first_last(case1, 99), [-1, -1])


def search_first_last(nums, k):
    LEFT, RIGHT = 0, 1

    def search(direction):
        i = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == k:
                i = m
                if direction == LEFT:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] > k:
                r = m - 1
            else:
                l = m + 1
        return i
    return [search(LEFT), search(RIGHT)]


unittest.main()
