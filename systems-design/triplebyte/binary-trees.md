---
description: 'https://gist.github.com/bshlgrs/cc35193f9a13bcf158b82a02aa261bbe'
---

# Binary Tree Implementations

## Red-black Trees

* **No two red nodes connected.** 
* **Every path to leaf contains same number of black nodes.** 
* Invariant: height of sibling subtrees differ by **max factor two.** 
* Re-balancing:
  * Worst case O\(logN\) to rotate up to parent. 
  * [https://www.cs.auckland.ac.nz/software/AlgAnim/AVL.html](https://www.cs.auckland.ac.nz/software/AlgAnim/AVL.html)
* Store color. 

## **A**delson-**V**elskii and **L**andis \(AVL\) Trees

* **No two sibling subtrees differ by more than 1 in height.** 
* Re-balancing: O\(1\). At most two rotations to fix deepest imbalance. 
* Store balance factor \(2 bits\) 

{% hint style="info" %}
"An extremely common misconception is “Balance means that you have similar numbers of nodes on the left and right side of the tree.” This is wrong. You only care about the _height_ of the left and right subtrees being similar, where height means the maximum distance to a leaf node. This doesn’t require similar numbers of nodes on the different sides of the trees. For example, suppose that you require that your two child nodes can’t have heights that differ by more than a factor of two. At maximum unbalance, your left child can have 2^h descendants and your right child can have 2^\(2h\) = 4^h descendants. The difference between 2^h and 4^h grows extremely rapidly as h grows. If your left child has a thousand elements, your right child can have a million elements \(that’s h = 10\)." 
{% endhint %}

## Comparison

* **Frequent insertions and deletions -&gt; red-black.**
  * RB tree rebalancing is O\(logN\),  but happens less often. 
* **Frequent search -&gt;  AVL.**
  * AVL trees are more balanced than RB \(differ by 1 vs factor of 2\), so faster lookup. 

