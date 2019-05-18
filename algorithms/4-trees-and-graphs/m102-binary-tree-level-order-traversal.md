# M102-binary-tree-level-order-traversal

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
We use zip and list comprehension for conciseness, but index counting may be faster. 

[1] Given the BF L2R traversals lt and rt of the left and right subtree of t respectively, the traversal of t is the merged [[t.val], <lt and rt merged>].

[2] We use zip_longest to take care of different lengths; fillvalue=[] means at depths that do not exist we can still safely merge. Take note it is a kwarg!


'''

from itertools import zip_longest


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        lt = self.levelOrder(root.left)
        rt = self.levelOrder(root.right)
        lr = zip_longest(lt, rt, fillvalue=[])  # [2]
        traversal = [[root.val]] + [l + r for l, r in lr]  # [1]
        return traversal

```

