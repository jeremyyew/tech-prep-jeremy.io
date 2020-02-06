# E100-same-tree

```python
class SolutionRec:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and \
            self.isSameTree(p.left, q.left) and \
            self.isSameTree(p.right, q.right)

# Note I use one stack here as opposed to the example during the session where I used two stacks.
# I also make the conditional branching more explicit than in the example (if-else instead of implicitly doing nothing) for readability, this is subjective.
# Lastly I also use 'p is None' as opposed to boolean coercion in the above i.e. 'not p', this is also subjective.  
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stk = [(p, q)]
        while stk:
            p, q = stk.pop()
            if p is None and q is None:
                continue
            elif p is None or q is None:
                return False
            else:
                if p.val != q.val:
                    return False
                else:
                    stk += [(p.right, q.right), (p.left, q.left)]
        return True
```

