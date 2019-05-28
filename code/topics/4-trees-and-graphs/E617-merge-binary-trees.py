# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Note: Easy to do if can mutate/reference inputs. Easy to do recursive non-mutation. Hard to do iterative + non-mutation.

# Recursive solution. Does not mutate inputs, returns new copy. Can be faster if modifies.
# Define the correct value at every subtree, with base case being None, None.


class SolutionRec:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode):
        curr = TreeNode(None)
        if t1 and t2:
            curr.val = t1.val + t2.val
            curr.left = self.mergeTrees(t1.left, t2.left)
            curr.right = self.mergeTrees(t1.right, t2.right)
        elif not t1 and t2:
            curr.val = t2.val
            curr.left = self.mergeTrees(None, t2.left)
            curr.right = self.mergeTrees(None, t2.right)
        elif t1 and not t2:
            curr.val = t1.val
            curr.left = self.mergeTrees(t1.left, None)
            curr.right = self.mergeTrees(t1.right, None)
        else:
            curr = None
        return curr

# Iterative solution: Use a stack for DF traversal (or queue for BF traversal).
# Also does not mutate inputs - returns new copy.


class SolutionIterative:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode):
        dummy = TreeNode(None)
        stk = [(t1, t2, dummy, 'l')]
        while stk:
            n1, n2, n3_parent, lr = stk.pop()
            n3 = TreeNode(None)
            if n1 or n2:
                if n1 and n2:
                    n3.val = n1.val + n2.val
                    stk += [(n1.left, n2.left, n3, 'l'),
                            (n1.right, n2.right, n3, 'r')]
                else:
                    n3.val = n1.val if n1 else n2.val
                    stk += [(n1.left if n1 else None,
                             n2.left if n2 else None, n3, 'l'),
                            (n1.right if n1 else None,
                             n2.right if n2 else None, n3, 'r')]
                if lr == 'l':
                    n3_parent.left = n3
                else:
                    n3_parent.right = n3
            else:
                if lr == 'l':
                    n3_parent.left = None
                if lr == 'r':
                    n3_parent.right = None
        return dummy.left


# Iterative solution 2: Possibly mutates inputs but faster and lesser parameters.

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode):
        if not t1:
            return t2
        if not t2:
            return t1
        stk = [(t1, t2)]
        while stk:
            n1, n2 = stk.pop()
            n1.val += n2.val

            if n1.left and n2.left:
                stk.append((n1.left, n2.left))
            elif not n1.left and n2.left:
                n1.left = n2.left

            if n1.right and n2.right:
                stk.append((n1.right, n2.right))
            elif not n1.right and n2.right:
                n1.right = n2.right
        return t1
