# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Conduct DF R-X-L traversal, keeping a cumulative sum that we add to every previous node. We have to do all the sums on the right before we can do the current node before we can do the sums on the left.
# Both versions modifies original input.


class SolutionWrite:
    # This version writes to shared memory.
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        if root is None:
            return root
        self.sumGreater(root)
        return root

    def sumGreater(self, t: TreeNode):
        # We never call sumGreater on a None tree.
        # Do sums on right subtree.
        if t.right:
            self.sumGreater(t.right)
        # Do sums on current node.
        t.val += self.sum
        self.sum = t.val
        # Do sums on left subtree.
        if t.left:
            self.sumGreater(t.left)


class Solution:
    # This solution returns the latest sum as a local parameter.
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        self.sumGreater(root, 0)
        return root

    def sumGreater(self, t: TreeNode, sum) -> int:
        # We never call sumGreater on a None tree.
        # Do sums on right subtree.
        if t.right:
            sum = self.sumGreater(t.right, sum)
        # Do sums on current node.
        t.val += sum
        sum = t.val
        # Do sums on left subtree.
        if t.left:
            sum = self.sumGreater(t.left, sum)
        return sum
