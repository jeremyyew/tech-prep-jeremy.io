# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
1. Filter Up: Most elegant and concise. 
    DF recursive, but returns trees only. 
    - Return root if root is p, q, or None
    - If one is in left, return left
    - If one is in right, return right
    - If both, return self. 
    
    This way, all subtrees which contain left or right eventually merge at their LCA, and the only value that 'filters up' to the original root node is the LCA, since every parent will pass the LCA up as a result (they only receive None from others). 

    See https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65225/4-lines-C%2B%2BJavaPythonRuby. 

2. DF recursive traversal, return containment, write to memory once found. Most simple and understandable.
    - O(N) time and space. 
    - Use coerced addition to count number of True values. 

3. Iterative DF search with Parent Pointers: Decently simple. No recursion. 
    O(N) time and space. 

4. Iterative Post-order Traversal with Parent Stack: Tricky. No pointers.
    O(N) time and space. 

'''


class Solution:
    def lowestCommonAncestor(self, node, p, q):
        def helper(node):
            if node in (None, p, q):
                return node
            l = helper(node.right)
            r = helper(node.left)
            return node if l and r else l or r
        return helper(node)


class SolutionRec:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        self.LCA = None

        def contains(root: 'TreeNode') -> bool:
            if root is None:
                return False
            l = contains(root.left)
            r = contains(root.right)
            m = (root.val == p.val) or (root.val == q.val)
            if l + r + m >= 2:
                self.LCA = root
            return l or r or m

        contains(root)
        return self.LCA


class SolutionParentPointer:
    def lowestCommonAncestor(self, root, p, q):
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q


class SolutionParentStack:
    BOTH_PENDING, LEFT_DONE, BOTH_DONE = 2, 1, 0

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack = [(root, SolutionParentStack.BOTH_PENDING)]
        one_node_found = False
        LCA_index = -1

        # We do a post order traversal of the binary tree using stack
        while stack:
            parent_node, parent_state = stack[-1]
            if parent_state != SolutionParentStack.BOTH_DONE:
                if parent_state == SolutionParentStack.BOTH_PENDING:
                    if parent_node == p or parent_node == q:
                        if one_node_found:
                            return stack[LCA_index][0]
                        else:
                            one_node_found = True
                            LCA_index = len(stack) - 1
                    child_node = parent_node.left
                else:
                    child_node = parent_node.right
                stack.pop()
                stack.append((parent_node, parent_state - 1))
                if child_node:
                    stack.append(
                        (child_node, SolutionParentStack.BOTH_PENDING))
            else:
                if one_node_found and LCA_index == len(stack) - 1:
                    LCA_index -= 1
                stack.pop()
        return None
