---
description: 'Merge sort, quick sort, bin sort, binary search, sorted merge.'
---

# 1. Searching and Sorting \(4M\)

```python
import unittest

class TestMergeSort(unittest.TestCase):
    def test_MergeSort(self):
        case1 = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5, 0]
        result1 = list(sorted(case1))
        case2 = [9, 1, 9, 1, 8, 3, 7, 4, 6, 5, 0]
        result2 = list(sorted(case2))

        mergeSort(case1)
        self.assertEqual(case1, result1)
        mergeSort(case2)
        self.assertEqual(case2, result2)


def mergeSort(arr):
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


class TestQuickSort(unittest.TestCase):
    def test_QuickSort(self):
        case1 = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5, 0]
        result1 = list(sorted(case1))

        case2 = [9, 1, 9, 1, 8, 3, 7, 4, 6, 5, 0]
        result2 = list(sorted(case2))

        quickSort(case1)
        self.assertEqual(case1, result1)
        quickSort(case2)
        self.assertEqual(case2, result2)


def quickSort(arr):
    def partition(l, r):  # l and r inclusive.
        pivot = arr[r]     # pivot
        for j in range(l, r):
            if arr[j] < pivot:
                arr[l], arr[j] = arr[j], arr[l]
                l += 1
        arr[l], arr[r] = arr[r], arr[l]
        return l

    def helper(l, r):  # l and r inclusive.
        if l >= r:
            return
        pi = partition(l, r)
        helper(l, pi-1)
        helper(pi+1, r)

    helper(0, len(arr) - 1)


class TestBinSort(unittest.TestCase):
    def test_BinSort(self):
        result1 = [0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
        case1 = [4, 5, 5, 3, 3, 4, 4, 5, 3, 4,5, 5, 0, 1, 2, 2]
        self.assertEqual(BinSort().sort(case1, None), result1)

        result2 = [2, 3, 3, 4, 4, 4, 5, 5, 5, 5]
        case2 = [5, 5, 5, 5, 4, 4, 4, 3, 3, 2]
        self.assertEqual(BinSort().sort(case2, None), result2)

        result3 = [(i // 10) for i in range(1000)]
        case3 = [i % 100 for i in range(1000)]
        self.assertEqual(BinSort().sort(case3, None), result3)


class BinSort():
    def sort(self, arr, comparator):
        self.freq = {}
        for e in arr: 
            if e in self.freq: 
                self.freq[e] += 1
            else: 
                self.freq[e] = 1

        keys = list(self.freq.keys())
        keys.sort(key=comparator) 
        groups = [[e] * self.freq[e] for e in keys]
        # print(groups)
        result = [e for group in groups for e in group]
        # print(result)
        return result

class TestBinarySearch(unittest.TestCase):
    def test_BinarySearchIterative(self):
        result1 = 42
        case1 = [i for i in range(100)]

        self.assertEqual(BinarySearchIterative().search(case1, 42), result1)
        self.assertIsNone(BinarySearchIterative().search(case1, 200))

    def test_BinarySearchRecursive(self):
        result1 = 42
        case1 = [i for i in range(100)]

        self.assertEqual(BinarySearchRecursive().search(case1, 42), result1)
        self.assertIsNone(BinarySearchRecursive().search(case1, 200))


class BinarySearchRecursive():
    def search(self, nums, x):
        def search_rec(l,r):
            if l > r: 
                return -1
            m = l + ((r-l) // 2)
            if nums[m] < x:
                l = m + 1
            elif nums[m] > x:
                r = m -1
            else: 
                return m
        return search_rec(0, len(nums)-1)


class BinarySearchIterative():
    def search(self, nums, k):
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


# Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B. Write a method to merge B into A in sorted order.

class TestSolution_10_1(unittest.TestCase):
    def testSortedMerge(self):
        A = [2, 4, 6, 8, 10, 12, None, None, None]
        B = [1, 3, 5]
        C = [1, 2, 3, 4, 5, 6, 8, 10, 12]
        self.assertEqual(SortedMerge().merge(A, B), C)
        A = [2, 4, 6, None, None, None,  None, None, None]
        B = [1, 3, 5, 7, 9, 11]
        C = [1, 2, 3, 4, 5, 6, 7, 9, 11]
        self.assertEqual(SortedMerge().merge(A, B), C)


class SortedMerge():
    def merge(self, A, B):
        self.A = A
        self.B = B
        shift_from = (len(self.A) - len(self.B)) - 1
        print(self.A)
        self.right_shift(shift_from, len(self.B))
        print(self.A)

        # Same as merge sort except we copy into A.
        # Invariant: for all current = i, we will not be overwriting an element of A that has not already been merged. 
        # For i from 0 to len(B) we only overwrite None. 
        # For i > len(B) where we have exceeeded len(B) by j elements, we will have merged at least j elements from A, since we have merged at most len(B)elements from B. Therefore we will have merged at least the first j elements of A, and the element A_i will be at least the (j + 1)th element.  
        A_index = len(B)
        B_index = 0
        current = 0
        while A_index < len(A) and B_index < len(B):
            if self.A[A_index] <= self.B[B_index]:
                self.A[current] = self.A[A_index]
                A_index += 1
            else: 
                self.A[current] = self.B[B_index]
                B_index += 1
            current += 1

        if B_index < len(B):
            while B_index < len(B):
                self.A[current] = self.B[B_index]
                B_index += 1
                current += 1
        # else: A is in place and we're done 

        return self.A

    def right_shift(self, start, offset):
        for i in range(start, -1, -1):
            self.A[i + offset] = self.A[i]


unittest.main()
```

