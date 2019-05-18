# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        while curr is not None:
            next_node = curr.next  # Save pointer to next node.
            curr.next = prev  # Point backwards to prev node.
            prev = curr  # Save current node to be pointed back to.
            curr = next_node  # Move to next node.
        return prev
