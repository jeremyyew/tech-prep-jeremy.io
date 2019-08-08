Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        pass

# Iterative mergesort function to 
# sort arr[0...n-1]  
def mergeSort(self, head): 
    current_size = 1
    left = head
    while left: 
        left = head
        while left: 
            mid = left + current_size - 1
            right = len(a) - 1 if 2 * current_size + left - 1 > len(a)-1 else 2 * current_size + left - 1
            mergeTwoLists(a, left, mid, right) 
            left = left.next
        current_size = 2 * current_size 
  
# Merge Function 

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