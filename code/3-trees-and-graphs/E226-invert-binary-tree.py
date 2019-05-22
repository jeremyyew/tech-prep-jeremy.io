# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class SolutionRec:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        # Save a pointer to left so that we dont overwrite and lose it.
        left = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(left)
        return root


class Solution:
    # Iterative version. Btw this is BF traversal.
    def invertTree(self, root: TreeNode) -> TreeNode:
        stk = []
        if root:
            stk.append(root)
        while stk:
            curr = stk.pop()
            left = curr.left
            curr.left = curr.right
            curr.right = left
            if curr.left:
                stk.append(curr.left)
            if curr.right:
                stk.append(curr.right)
        return root
