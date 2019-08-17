# M105-construct-binary-tree-from-preorder-and-inorder-traversal

[https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34680/Python%3A-Recursion-version-and-Iteration-version-easy-to-understand](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34680/Python%3A-Recursion-version-and-Iteration-version-easy-to-understand)

```python
from collections import deque

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return
        preorder = deque(preorder)
        indexes = {n: i for i, n in enumerate(inorder)}
        root = TreeNode(None)
        stack = [(root, 0, len(inorder))]
        while stack and preorder:
            node, l, r = stack.pop()
            node.val = preorder.popleft()
            i = indexes[node.val]
            if i+1 < r:
                node.right = TreeNode(None)
                stack.append((node.right, i+1, r))
            if l < i:
                node.left = TreeNode(None)
                stack.append((node.left, l, i))
        return root


# r = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
# print(r)


class SolutionRecIndex:
    def buildTree(self, preorder, inorder):
        indexes = {n: i for i, n in enumerate(inorder)}

        def build(l, r):
            if l >= r:
                return
            val = preorder.pop(0)  # use deque to avoid O(N)
            i = indexes[val]
            root = TreeNode(val)
            root.left = build(l, i)
            root.right = build(i+1, r)
            return root
        return build(0, len(inorder))


class SolutionRecSlice:
    def buildTree(self, preorder, inorder):
        if not inorder:
            return
        val = preorder.pop(0)
        i = inorder.index(val)
        root = TreeNode(inorder[i])
        root.left = self.buildTree(preorder, inorder[0:i])
        root.right = self.buildTree(preorder, inorder[i+1:])
        return root

```

