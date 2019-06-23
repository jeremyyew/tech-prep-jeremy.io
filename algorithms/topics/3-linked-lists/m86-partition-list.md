# M86-partition-list

* Traverse the list while building two new linked lists, one smaller and one bigger \(they're not really new since you're just changing pointers on existing nodes\).
* Then append them. 
* Definitely use dummy nodes to avoid having to check for edge cases later.

```python
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None
        l = l_start = ListNode(None)
        r = r_start = ListNode(None)
        while head: 
            if head.val < x:
                l.next = head 
                l = l.next 
            else:  
                r.next = head 
                r = r.next 
            head = head.next 
        r.next = None    
        l.next = r_start.next
        return l_start.next
```

