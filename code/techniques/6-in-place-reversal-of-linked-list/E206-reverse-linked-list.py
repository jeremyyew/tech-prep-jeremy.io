# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseList(self, head):
        prev_node = None
        curr_node = head
        while curr_node is not None:
            next_node = curr_node.next  # Save pointer to next node.
            curr_node.next = prev_node  # Point backwards to prev node.
            prev_node = curr_node  # Save current node to be pointed back to.
            curr_node = next_node  # Move to next node.
        return prev_node
