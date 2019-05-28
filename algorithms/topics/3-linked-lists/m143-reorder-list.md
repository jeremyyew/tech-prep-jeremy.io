# M143-reorder-list

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
[1] Use slow/fast pointer to divide list into L and R, and return R. 
[2] Reverse R.
[3] Merge L and reversed R.
[4] Check case of single-element list explicitly in main body. Otherwise merge will loop trying to merge list to itself (it's not obvious that merge shold be responsible for checking that).

- Our divideList MUST delete the link between L and R, otherwise merge will not know when to end. 
'''


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        R = self.divideList(head)  # [1]
        if R == head:
            return  # [4]
        revR = self.reverseList(R)  # [2]
        self.mergeTwoLists(head, revR)  # [3]

    def divideList(self, head: ListNode) -> ListNode:
        prev = slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next = None
        return slow

    def reverseList(self, head):
        prev = None
        curr = head
        while curr is not None:
            next_node = curr.next  # Save pointer to next node.
            curr.next = prev  # Point backwards to prev node.
            prev = curr  # Save current node to be pointed back to.
            curr = next_node  # Move to next node.
        return prev

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        head = l1
        while l1 and l2:
            l1_temp = l1.next
            l1.next = l2
            l1 = l1.next
            l2 = l1_temp
        return head

```

