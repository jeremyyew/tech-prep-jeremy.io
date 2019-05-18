# M114-flatten-binary-tree

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        current = root
        while True: 
            # traverse to rightmost node with left branch
            while current.left is None:
                if current.right is None:
                    return
                current = current.right
            
            # save right branch if necessary
            temp_r = None # reset to None
            if current.right is not None:
                temp_r = current.right
                
            # shift left branch to right node
            current.right = current.left
            # save current node so we can return to it 
            temp_current = current.right 
            # delete left branch
            current.left = None
            # append right branch at rightmost node, if necessary
            if temp_r is not None:
                while current.right is not None:
                    current = current.right
                # put rest of right branch here 
                current.right = temp_r
            # reset current to level of tree in outer loop 
            current = temp_current
```

