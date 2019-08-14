# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class SolutionRec:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and \
            self.isSameTree(p.left, q.left) and \
            self.isSameTree(p.right, q.right)


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stk_p, stk_q = [p], [q]
        while stk_p and stk_q:
            p, q = stk_p.pop(), stk_q.pop()
            if (not p and q) or (p and not q):
                return False
            if p and q:
                if p.val != q.val:
                    return False
                stk_p += [p.left, p.right]
                stk_q += [q.left, q.right]
        return True
