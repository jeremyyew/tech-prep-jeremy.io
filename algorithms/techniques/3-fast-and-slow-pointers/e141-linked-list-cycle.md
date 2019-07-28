# E141-linked-list-cycle

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head 
        while fast is not None:
            if fast.next is None:
                return False
            fast = fast.next.next 
            slow = slow.next
            if fast is slow: 
                return True
        return False
```

