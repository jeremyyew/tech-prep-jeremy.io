# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
In order to check if a tree t is valid, it's not enough to know that the left and right subtrees l and r are valid, or to simply check their node values. We need to also check:
    - max value in l < t.val
    - min value in r > t.val

For the recursive approach, we can:
    - pass down upper and lower limits as parameters and receive validity boolean (we use inf or negative inf for the root node)
    - return min and max values along with validity (passing None if there is a false). 

The solution used is the latter, with O(N) time and space. 

See https://leetcode.com/problems/validate-binary-search-tree/solution/

'''


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        _, _, valid = self.validate(root)
        return valid

    def validate(self, root):
        if root is None:
            return None, None, True

        lmin, lmax, lvalid = self.validate(root.left)
        rmin, rmax, rvalid = self.validate(root.right)

        if not lvalid or not rvalid:
            return None, None, False

        if lmax and root.val <= lmax:
            return None, None, False

        if rmin and root.val >= rmin:
            return None, None, False

        minimum, maximum = root.val, root.val
        if lmin:
            minimum = lmin
        if rmax:
            maximum = rmax

        return minimum, maximum, True


class SolutionBounds:
    def isValidBST(self, root):
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)


class SolutionIterative:
    def isValidBST(self, root):
        if not root:
            return True

        stack = [(root, float('-inf'), float('inf')), ]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True


class SolutionInOrderTraversal:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True
