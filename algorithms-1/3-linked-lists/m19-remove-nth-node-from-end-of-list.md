# M19-remove-nth-node-from-end-of-list

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
We have pointer a and 'ahead' pointer b by n+1 steps. When b terminates, we are right before intended removal node. 

[1] We need to move b ahead by n+1, so that when b terminates, we are right before intended removal node, not at it. 
[2] Then we can always access a.next.next. 
[3] We need a dummy node so b can travel n+1 steps. Otherwise b might try to access None.next. 

[3] Base case None: should not get. If stated, explicit check at the start. 
[4] Base case 1 element: See 1. 
'''


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(None)
        a = b = dummy  # [3]
        dummy.next = head
        for _ in range(n + 1):  # [1]
            b = b.next

        while b:
            a = a.next
            b = b.next

        a.next = a.next.next  # [2]

        return dummy.next

```

