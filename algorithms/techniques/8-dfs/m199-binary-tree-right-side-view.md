# M199-binary-tree-right-side-view

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        if not root: 
            return []
        view, stk = [], [(root, 0)]
        while stk: 
            node, depth = stk.pop()
            if depth + 1 > len(view):
                view.append(node.val)
            else: 
                view[depth] = node.val 
            if node.right:
                stk.append((node.right, depth + 1))
            if node.left: 
                stk.append((node.left, depth + 1))
        
        return view
```

