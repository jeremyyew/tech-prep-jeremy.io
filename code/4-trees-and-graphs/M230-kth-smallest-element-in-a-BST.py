# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
We need an in-order traversal, which stops once we've obtained the kth smallest number.

Depth-first LMR traversal using a stack gives us inorder traversal. The intuition is that for some tree t, we process the entire left subtree first, then add the middle, then process the right subtree. Then we return to the parent of t via the stack. 

[0] Begin with root in stack. 

[1] Pop new root from stack.
[2] L: Push all left subtrees to stack (depth first traversal).
[3] M: Pop most recent left node, add to inorder list. 
[5] R: Push right subtree on stack. 
'''


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = [root]
        inorder = []
        while stack and len(inorder) < k:
            node = stack.pop()
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            inorder.append(node.val)
            stack.append(node.right)
        return inorder[k-1]
