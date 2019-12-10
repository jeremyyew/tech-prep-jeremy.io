class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float("-inf")

        def dfs(root):
            if not root:
                return 0
            l = max(dfs(root.left), 0)
            r = max(dfs(root.right), 0)
            val = l + root.val + r
            self.max_sum = max(self.max_sum, val)
            return root.val + max(l, r)
        dfs(root)
        return self.max_sum
