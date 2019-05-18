# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return None
        serial = "{},{},{}".format(root.val,
                                   self.serialize(root.left),
                                   self.serialize(root.right))
        return serial

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))
        nodes = data.split(",")
        return self.constructTree(nodes)

    def constructTree(self, nodes):
        head = TreeNode(None)
        head.val = nodes[0]
        m = (len(nodes) - 1)//2
        head.left = self.deserialize(nodes[1:m])
        head.right = self.deserialize(nodes[m:])
        return head
