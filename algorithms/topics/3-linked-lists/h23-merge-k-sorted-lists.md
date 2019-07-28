# H23-merge-k-sorted-lists

* **Brute force**: Compare the heads of all lists to get the min. Update the head of the min-value list, and repeat. `O(k * N)` where `k` is num of lists, and `N` is total number of nodes.  
* We need to **maintain an ordered queue of the value of the current heads of all lists**. Each time we will pop the min-value node and append it to our result, and we will also update the queue with the next node of that min-value list. 
* So we use a heap. 
* Time complexity: `heapify: O(k)` + `N` pushes and pops of heap size `k`: `O(N * logk)` = `O(Nlogk)`.

```python
from typing import List
import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = node = ListNode(None)
        h = [(node.val, i, node)
             for i, node in enumerate(lists) if node]
        heapq.heapify(h)

        while h:
            # print(h)
            _, i, min_node = heapq.heappop(h)
            node.next = min_node
            node = node.next
            # print(node.val)
            if min_node.next:
                heapq.heappush(h, (min_node.next.val, i, min_node.next))
        return head.next


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#     def fromArray(self, nums):
#         head = node = ListNode(None)
#         for x in nums:
#             node.next = ListNode(x)
#             node = node.next
#         return head.next

# a = ListNode(object).fromArray([1, 5, 9, 13])
# b = ListNode(object).fromArray([2, 6, 10, 14])
# c = ListNode(object).fromArray([3, 7, 11, 15])
# d = ListNode(object).fromArray([4, 8, 12, 16])
# r = Solution().mergeKLists([a, None, b, c, d, None])

```



