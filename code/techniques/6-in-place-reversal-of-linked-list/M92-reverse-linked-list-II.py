'''
- **To achieve one-pass: save the end of the prefix, and what will be the end of the reversed sequence, i.e. `node_m_minus_one` and `node_m`**. 
    - `node_m_minus_one` is right before the reversed sequence, so later we will point it to the start of the reversed sequence. 
    - `node_m` is the end of the reversed sequence, so later we will point it to the rest of the list.  
    - Point backwards for all  `m < i <= n`.
    - When `i == n`:
        - point `node_m_minus_one -> node_n`
        - point `node_m -> node_n.next`
- In case of `m == n`, we wouldn't reach a conditional`i == m` since we'd hit `i == n` instead. This is just due to the branching. So it actually is crucial in this case to assign both `node_m_minus_one` and `node_m` at once, else `node_m` would not be assigned. 
    - The important thing to note is: **what do we do when `m == n`?** Because that will definitely trip you up. 
- In the case of `m == 1`, we will also need a dummy head at index 0 to maintain a pointer to the start.
'''


class Solution:
    def reverseBetween(self, head, m, n):
        # if m == n:
        #     return head
        node = dummy = ListNode(None)
        dummy.next = head
        prev_node, i = None, 0
        while node:
            next_node = node.next
            if i < n:
                if i == m - 1:
                    node_m_minus_one = node
                    node_m = next_node
                elif m < i < n:
                    node.next = prev_node
                prev_node = node
                node = next_node
                i += 1
            else:
                node.next = prev_node
                node_m_minus_one.next = node
                node_m.next = next_node
                break
        return dummy.next


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#     def fromList(self, nums):
#         head = node = ListNode(None)
#         for x in nums:
#             node.next = ListNode(x)
#             node = node.next
#         return head.next

#     @staticmethod
#     def toList(node):
#         l = []
#         i = 0
#         while node and i < 11:
#             i += 1
#             l.append(node.val)
#             node = node.next
#         return l


# a = ListNode(object).fromList([1, 2, 3, 4, 5])
# r = Solution().reverseBetween(a, 2, 4)
# print(ListNode.toList(r))
