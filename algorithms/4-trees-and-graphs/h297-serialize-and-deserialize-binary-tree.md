# H297-serialize-and-deserialize-binary-tree

To serialize, we **append** to a string while using **depth-first pre-order \(XLR\) traversal.**  
To deserialize, we simply reconstruct the tree in **depth-first pre-order \(XLR\)** as well, **dequeing** i.e. popping from the front of the string \(or reverse and pop from the end\).

Example: `[1,2,3,null,null,4,5]` -&gt; `'1,2,None,None,3,4,None,None,5,None,None,'`

\[1\] Remember to strip the trailing comma from serialized string.

```python
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
        def buildString(node):
            if node is None:
                self.s += 'None,'
            else:
                self.s += f'{node.val},'
                buildString(node.left)
                buildString(node.right)
        self.s = ''
        buildString(root)
        return self.s.rstrip(',')  # [1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def buildTree():
            val = self.nodes.pop(0)
            if val == 'None':
                return None
            else:
                node = TreeNode(int(val))
                node.left = buildTree()
                node.right = buildTree()
                return node
        self.nodes = data.split(',')
        return buildTree()

```

