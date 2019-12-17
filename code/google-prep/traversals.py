
class Node():
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def inorder_rec(node):
    if node is None:
        return
    inorder_rec(node.left)
    print(node.val)
    inorder_rec(node.right)


def inorder_iter(node):
    if node is None:
        return
    stk = []
    while True:
        while node:
            stk.append(node)
            node = node.left
        if not stk:
            break
        node = stk.pop()
        print(node.val)
        node = node.right


def preorder_rec(node):
    if not node:
        return
    print(node.val)
    preorder_rec(node.left)
    preorder_rec(node.right)


def preorder_iter(node):
    if not node:
        return
    stk = []
    while True:
        while node:
            print(node.val)
            if node.right:
                stk.append(node.right)
            node = node.left
        if not stk:
            break
        node = stk.pop()


def postorder_rec(node):
    if not node:
        return
    postorder_rec(node.left)
    postorder_rec(node.right)
    print(node.val)


def postorder_iter(root):
    if not root:
        return
    s1, s2 = [], []
    s1.append(root)
    while s1:
        node = s1.pop()
        s2.append(node.val)
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
    print(s2[::-1])


t1, t2, t3, t4, t5 = [Node(x) for x in range(1, 6)]
t4.left = t2
t4.right = t5
t2.left = t1
t2.right = t3

# inorder_rec(t4)
# inorder_iter(t4)
# preorder_rec(t4)
# preorder_iter(t4)
postorder_rec(t4)
postorder_iter(t4)
