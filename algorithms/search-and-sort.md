---
description: 'Merge sort, quick sort, bin sort, binary search, sorted merge.'
---

# Searching and Sorting Basics

```python
import unittest

class TestMergeSort(unittest.TestCase):
    def test_MergeSort(self):
        result1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        case1 = [10, 1, 9, 2, 8 ,3, 7, 4, 6, 5, 0]

        result2 = [0, 1, 1, 3, 4, 5, 6, 7, 8, 9, 9]
        case2 = [9, 1, 9, 1, 8 ,3, 7, 4, 6, 5, 0]


        self.assertEqual(MergeSort().mergeSort(case1), result1)
        self.assertEqual(MergeSort().mergeSort(case2), result2)


class MergeSort():
    def mergeSort(self, arr):
        self.helper = [None] * len(arr)
        self.arr = arr
        self.sort(0, len(arr) - 1)
        return self.arr

    def sort(self, start, end):
        # print(f'arr: {arr}, start: {start}, end: {end}')
        if start >= end:
            return
        mid = (start + end) // 2
        self.sort(start, mid)
        self.sort(mid + 1, end) # The plus one is super important, else you get infinite loop
        self.merge(start, mid, end)

    def merge(self, start, mid, end):
        # Copy both halves into a helper array. 
        # We can safely access the class members because our recursion will copy and merge in the correct order (left to right, bottom up).
        for i in range(start, end + 1):
            self.helper[i] = self.arr[i]

        left = start
        right = mid + 1 
        current = start

        # Iterate through helper array. Compare the left and right half, copying back the smaller element from the two halves into the original array.
        while left <= mid and right <= end: 
            if self.helper[left] <= self.helper[right]:
                self.arr[current] = self.helper[left]
                left += 1
            else:   
                self.arr[current] = self.helper[right]
                right += 1
            current += 1

        #  Either LHS or RHS arr will still have remaining elements, which now simply need to be appended. However, we only need to continue copying if the remaining elements are on LHS - otherwise RHS elements are already there. 
        remaining = mid - left
        for i in range(0, remaining + 1):
            self.arr[current + i] = self.helper[left + i]


class TestQuickSort(unittest.TestCase):
    def test_QuickSort(self):
        result1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        case1 = [10, 1, 9, 2, 8 ,3, 7, 4, 6, 5, 0]

        result2 = [0, 1, 1, 3, 4, 5, 6, 7, 8, 9, 9]
        case2 = [9, 1, 9, 1, 8 ,3, 7, 4, 6, 5, 0]

        self.assertEqual(QuickSort().quickSort(case1), result1)
        self.assertEqual(QuickSort().quickSort(case2), result2) 

class QuickSort(): 
    def quickSort(self, arr):
        self.arr = arr
        self.sort(0, len(arr) - 1)
        return self.arr

    def sort(self, left, right):
        index = self.partition(left, right)
        # print(self.arr)
        if left < index - 1: # Sort left half 
            self.sort(left, index - 1)
        if index < right: # Sort right half
            self.sort(index, right)

    def partition(self, left, right):
        pivot = self.arr[(left + right)//2]
        # In order to swap in place, we need to find pairs that are both on the wrong side.
        # Keep going to the middle. 
        while left <= right:
            # starting from left, look for the index of the next LHS value greater than partition
            while self.arr[left] < pivot and left <= right: 
                left += 1 
            # vice-versa for RHS
            while self.arr[right] > pivot and left <= right: 
                # print(f'right: {right}, len: {len(self.arr)}')
                right -= 1
            # Swap. But check if left is still <= right. 
            if left <= right: 
                temp = self.arr[left]
                self.arr[left] = self.arr[right]
                self.arr[right] = temp
                left += 1
                right -= 1
        return left


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

class BinarySearchIterative():
    def search(self, arr, x):
        start, end = 0, len(arr) - 1 
        while start <= end: 
            mid = (start + end) // 2
            if arr[mid] < x:
                start = mid + 1
            elif arr[mid] > x:
                end = mid -1
            else: 
                return mid
        return None


class BinarySearchRecursive():
    def search(self, arr, x):
        self.x = x
        self.arr = arr
        return self.search_rec(0, len(arr) - 1)

    def search_rec(self, start, end):
        # print(start, end)
        if start > end: 
            return None
        mid = (start + end) // 2
        if self.arr[mid] < self.x:
            start = mid + 1
        elif self.arr[mid] > self.x:
            end = mid -1
        else: 
            return mid
        return self.search_rec(start, end)


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

