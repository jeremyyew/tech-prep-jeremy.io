# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_diameter, _ = self.maxDiameterAndDepth(root)
        return max_diameter

    def maxDiameterAndDepth(self, t: TreeNode) -> (int, int):
        # The not-so-nice aspect of this computation is that both nones and their parents have 0 diameter and height. I do this to avoid having multiple if-else branches to check if left and right exist.
        if t is None:
            return 0, 0
        l_max_diameter, l_max_depth = self.maxDiameterAndDepth(t.left)
        r_max_diameter, r_max_depth = self.maxDiameterAndDepth(t.right)
        # We only add edges if there are children.
        diameter = l_max_depth + r_max_depth + \
            (1 if t.left else 0) + (1 if t.right else 0)
        max_diameter = max(l_max_diameter, r_max_diameter, diameter)
        # We only add to height if there are children.
        max_depth = max(r_max_depth, l_max_depth) + \
            (1 if t.left or t.right else 0)
        return max_diameter, max_depth
