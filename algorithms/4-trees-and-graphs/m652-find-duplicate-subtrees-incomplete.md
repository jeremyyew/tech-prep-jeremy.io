# M652-find-duplicate-subtrees

```python
import collections

'''
 Don't try to keep track of comparisons while traversing the tree, its messy and almost impossible - particularly since every step you have to make new comparisons, while you still have a pending comparison on the other subtree to make.

 Keep it simple - serialize and you have something easily comparable. It's O(1) lookup since we can map the serialized trees. That gives total O(n) from traversal of all nodes.  
'''


class Solution(object):
    def findDuplicateSubtrees(self, root):
        count = collections.Counter()
        dups = []

        def traverse(t):
            if not t:
                return None
            serial = "{},{},{}".format(
                t.val, traverse(t.left), traverse(t.right))
            count[serial] += 1
            if count[serial] == 2:
                dups.append(t)
            return serial

        traverse(root)
        return dups

```

