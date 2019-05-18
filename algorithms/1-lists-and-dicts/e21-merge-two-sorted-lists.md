# E21-merge-two-sorted-lists

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#     def createArray(self, nums):
#         l = None
#         head = None
#         for x in nums: 
#             if l is None:
#                 l = ListNode(x)
#                 head = l
#             else: 
#                 l.next = ListNode(x)
#                 l = l.next
#         return head

# a = ListNode(object).createArray([1, 3, 5, 7, 9])
# b = ListNode(object).createArray([2, 4, 6, 8, 10])


# This solution has been optimized for readability and conciseness. It can be faster if we check for None before and after the while loop, with the while loop terminating if either are None, but in the end its the same time complexity. 
# Also remember we can use dummy node so that we dont have to check if node is null initially. 
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node = ListNode(None)
        head = node

        while True: # better than a termination condition, because its tricky to refactor the code to pop the list for the next iteration to check, when you can't keep a reference to which list you want to pop at the end.
            print(node.val)
            if l1 is None and l2 is None: 
                return 
             # there is at least one non-None
            if l1 is None or l2 is None: 
                if l1 is None: 
                    some = l2
                else: 
                    some = l1
                node.next = some
                return head.next
            # both are non-None
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next 
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        return head.next


# Solution().mergeTwoLists(a, b)
```

