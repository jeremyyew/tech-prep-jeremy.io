# E235-lowest-common-ancestor-of-a-binary-search-tree

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
BST ordered property helps us determine if p and q are in left subtree or right subtree or both. 

The iterative version is slightly shorter, since we don't have to use a stack or recursion because we dont have to return to previous nodes. 

[1] If both p and q are on left, then continue search on left.
[2] ElIf both p and q are on right, then continue search on right.
[3] Else one if left and one is right, and we have found LCA. 

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solution/
'''


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        node = root
        while node:
            if p.val > node.val and q.val > node.val:
                node = node.right
            elif p.val < node.val and q.val < node.val:
                node = node.left
            else:
                return node


class SolutionRecursive:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None
        if (p.val < root.val and q.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (p.val > root.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

```

