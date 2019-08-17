# M133-clone-graph

* Two main challenges: 
* **Avoid duplicate traversals/cloning \(instead, point to already-cloned object\)**.
  * Dictionary with original node objects as keys, and cloned objects as value. 
  * Always check, and reference the clone if already cloned. 
* **Clone a node and then all its neighbors, and all their neighbors, etc.**
  * We can use either recursion or stack/queue \(DFS/BFS, no difference\). 
  * **Recursive**: 
    * We first make the clone of the current node without neighbors. 
    * Then, we make a recursive call for each of the node's neighbor, to make sure it and all its neighbors have been cloned, before appending it to the current clone's neighbors. 
  * **Iterative**: 
    * For each node that we pop from the stack, we assume it has been cloned but without neighbors. We just need to clone each of its neighbors and append them \(and also push them on the stack\).

      and then put the original node on the stack, and later we will 

    * We put the original node on the stack instead of its neighbors even though we are really iterating over the neighbors, just so we can replace the neighbors reference within the node, but really we can slice-overwrite the neighbors list if we wanted. 
  * The recursive version is DFS at the node level - it will recursive clone all the leftmost neighbors at all depths before moving on the other neighbors from bottom up. 
  * The iterative version is DFS but at neighbors level - it will clone all the immediate neighbors of the current node, and then all the immediate neighbors of the most recent node at the current depth. 

```python

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        root_clone = Node(node.val, [])
        stk, cloned = [node], {node: root_clone}
        while stk:
            node = stk.pop()
            for nb in node.neighbors:
                if nb not in cloned:
                    cloned[nb] = Node(nb.val, [])
                    cloned[node].neighbors.append(cloned[nb])
                    stk.append(nb)
                else:
                    cloned[node].neighbors.append(cloned[nb])
        return root_clone


class SolutionRec:
    def cloneGraph(self, node):
        cloned = {}

        def cloneHelper(node):
            if node and node not in cloned:
                cloned[node] = Node(node.val, [])
                cloned[node].neighbors = [cloned.get(nb) or
                                          cloneHelper(nb) for nb in node.neighbors]
                return cloned[node]
        return cloneHelper(node)

```

