# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class SolutionRec:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1

# Here we use shared memory to achieve tail recursion. We could also do iterative to have no recursion. Note python's stdlib max is O(n).


class Solution:
    def writeMaxDepth(self, node: TreeNode, depth):
        if node is not None:
            self.writeMaxDepth(node.left, depth + 1)
            self.writeMaxDepth(node.right, depth + 1)
        else:
            self.max_depth = max(self.max_depth, depth)

    def maxDepth(self, root: TreeNode) -> 'int':
        if root is None:
            return 0
        self.max_depth = 0
        self.writeMaxDepth(root.left, 1)
        self.writeMaxDepth(root.right, 1)
        return self.max_depth
