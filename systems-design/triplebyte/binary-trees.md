---
description: 'https://gist.github.com/bshlgrs/cc35193f9a13bcf158b82a02aa261bbe'
---

# Binary Tree Implementations

## Balancing trees 

* Search and modification proportional to height. So keep height at O\(logN\).  

### Red-black Trees

* Rules: 
  * No two red nodes connected. 
  * Every path to leaf contains same number of black nodes. 
* Invariant: **height of sibling subtrees differ by max factor two**. 
* Property: Height is only a constant multiple of log\(n\). 
* Re-balancing: Amortized O\(1\). Why? 
  * O\(1\) to restructure. 
  * O\(logN\) to recolor, which is recursive. But amortized O\(1\). 
  * [https://www.cs.auckland.ac.nz/software/AlgAnim/AVL.html](https://www.cs.auckland.ac.nz/software/AlgAnim/AVL.html)

{% hint style="info" %}
"An extremely common misconception is “Balance means that you have similar numbers of nodes on the left and right side of the tree.” This is wrong. You only care about the _height_ of the left and right subtrees being similar, where height means the maximum distance to a leaf node. This doesn’t require similar numbers of nodes on the different sides of the trees. For example, suppose that you require that your two child nodes can’t have heights that differ by more than a factor of two. At maximum unbalance, your left child can have 2^h descendants and your right child can have 2^\(2h\) = 4^h descendants. The difference between 2^h and 4^h grows extremely rapidly as h grows. If your left child has a thousand elements, your right child can have a million elements \(that’s h = 10\)." 
{% endhint %}

### **A**delson-**V**elskii and **L**andis \(AVL\) Trees

* Rules: 
  * No two sibling subtrees differ by more than 1 in height. 
* Invariant: **height of sibling subtrees differ by max factor two**. 
* Property: Height is only a constant multiple of log\(n\). 
* Re-balancing: log\(N\) since we may have to rebalance parents as well, up to the root. 

## Comparison

* AVL trees are more balanced. 
* AVL trees require more rotations than red-black. 
* Frequent insertions and deletions -&gt; red-black.
* Frequent search -&gt;  AVL. 

