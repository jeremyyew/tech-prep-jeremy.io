import collections

'''
 Don't try to keep track of comparisons while traversing the tree, its messy and almost impossible - particularly since every step you have to make new comparisons, while you still have a pending comparison on the other subtree to make.


1. Serialize. O(N^2) time, O(N^2) space. 
     Keep it simple - serialize subtrees and concatenate to get serialization of parent nodes. 

2. UID. O(N) time, O(N) time.
    Use (parent_id, left_id, right_id) as UID. 
    Use defaultdict() and default_factory to get a dict with default values. Use len to get unique values (assuming that is the only thing you ever use to initialize new key-value pairs).
'''


class SolutionSerialize(object):
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


class Solution(object):
    def findDuplicateSubtrees(self, root):
        trees = collections.defaultdict()
        trees.default_factory = trees.__len__
        count = collections.Counter()
        ans = []

        def lookup(node):
            if node:
                uid = trees[node.val, lookup(node.left), lookup(node.right)]
                count[uid] += 1
                if count[uid] == 2:
                    ans.append(node)
                return uid

        lookup(root)
        return ans
