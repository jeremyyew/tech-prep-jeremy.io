
class Node():
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def inorder_rec(node):
    if not node:
        return
    inorder_rec(node.left)
    print(node.val, end="")
    inorder_rec(node.right)


def inorder_iter(node):
    '''
    LMR. Append curr, and go left til nothing. Pop and print, then go right.
    Any node popped from top of stack has left subtree already processed.
    '''
    stk = []
    while True:
        while node:
            stk.append(node)
            node = node.left
        if not stk:
            break
        node = stk.pop()
        print(node.val, end="")
        node = node.right


def preorder_rec(node):
    if not node:
        return
    print(node.val, end="")
    preorder_rec(node.left)
    preorder_rec(node.right)


def preorder_iter(node):
    '''
    MLR. Print curr, append R, and go left.
    Any node popped from top of stack has parent (if any) and left sibling already processed.
    '''
    stk = []
    while True:
        while node:
            print(node.val, end="")
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
    print(node.val, end="")


def postorder_iter(root):
    '''
    LRM.
    Start with root in s1.
    Pop s1 and append to s2.
    Append left THEN right child to s1. Repeat.
    '''
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
    for n in s2[::-1]:
        print(n, end="")


def bfs(root):
    if not root:
        return
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.val, end="")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


t1, t2, t3, t4, t5 = [Node(x) for x in range(1, 6)]
t4.left = t2
t4.right = t5
t2.left = t1
t2.right = t3

print("\nshould be:\n12345")
inorder_rec(t4)
print("\nshould be:\n12345")
inorder_iter(t4)
print("\nshould be:\n42135")
preorder_rec(t4)
print("\nshould be:\n42135")
preorder_iter(t4)
print("\nshould be:\n13254")
postorder_rec(t4)
print("\nshould be:\n13254")
postorder_iter(t4)
print("\nshould be:\n42513")
bfs(t4)
