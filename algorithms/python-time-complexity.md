# Python Time Complexity

## List 

| **Operation** | **Average Case** | [**Amortized Worst Case**](http://en.wikipedia.org/wiki/Amortized_analysis) |
| :--- | :--- | :--- |
| Copy | O\(n\) | O\(n\) |
| Append\[1\] | O\(1\) | O\(1\) |
| Pop last | O\(1\) | O\(1\) |
| Pop intermediate | O\(k\) | O\(k\) |
| Insert | O\(n\) | O\(n\) |
| Get Item | O\(1\) | O\(1\) |
| Set Item | O\(1\) | O\(1\) |
| Delete Item | O\(n\) | O\(n\) |
| Iteration | O\(n\) | O\(n\) |
| Get Slice | O\(k\) | O\(k\) |
| Del Slice | O\(n\) | O\(n\) |
| Set Slice | O\(k+n\) | O\(k+n\) |
| Extend\[1\] | O\(k\) | O\(k\) |
| [Sort](http://svn.python.org/projects/python/trunk/Objects/listsort.txt) | O\(n log n\) | O\(n log n\) |
| Multiply | O\(nk\) | O\(nk\) |
| x in s | O\(n\) |  |
| min\(s\), max\(s\) | O\(n\) |  |
| Get Length | O\(1\) | O\(1\) |

## collections.deque

A deque \(double-ended queue\) is represented internally as a doubly linked list. Both ends are accessible, but even looking at the middle is slow, and adding to or removing from the middle is slower still.

| **Operation** | **Average Case** | **Amortized Worst Case** |
| :--- | :--- | :--- |
| Copy | O\(n\) | O\(n\) |
| append | O\(1\) | O\(1\) |
| appendleft | O\(1\) | O\(1\) |
| pop | O\(1\) | O\(1\) |
| popleft | O\(1\) | O\(1\) |
| extend | O\(k\) | O\(k\) |
| extendleft | O\(k\) | O\(k\) |
| rotate | O\(k\) | O\(k\) |
| remove | O\(n\) | O\(n\) |

## Set <a id="set"></a>

See dict -- the implementation is intentionally very similar.

| **Operation** | **Average case** | **Worst Case** | **notes** |
| :--- | :--- | :--- | :--- |
| x in s | O\(1\) | O\(n\) |  |
| Union s\|t | [O\(len\(s\)+len\(t\)\)](https://wiki.python.org/moin/TimeComplexity_%28SetCode%29) |  |  |
| Intersection s&t | O\(min\(len\(s\), len\(t\)\) | O\(len\(s\) \* len\(t\)\) | replace "min" with "max" if t is not a set |
| Multiple intersection s1&s2&..&sn |  | \(n-1\)\*O\(l\) where l is max\(len\(s1\),..,len\(sn\)\) |  |
| Difference s-t | O\(len\(s\)\) |  |  |
| s.difference\_update\(t\) | O\(len\(t\)\) |  |  |
| Symmetric Difference s^t | O\(len\(s\)\) | O\(len\(s\) \* len\(t\)\) |  |

## Dict <a id="dict"></a>

The Average Case times listed for dict objects assume that the hash function for the objects is sufficiently robust to make collisions uncommon. The Average Case assumes the keys used in parameters are selected uniformly at random from the set of all keys.

| **Operation** | **Average Case** | **Amortized Worst Case** |
| :--- | :--- | :--- |
| Copy\[2\] | O\(n\) | O\(n\) |
| Get Item | O\(1\) | O\(n\) |
| Set Item\[1\] | O\(1\) | O\(n\) |
| Delete Item | O\(1\) | O\(n\) |
| Iteration\[2\] | O\(n\) | O\(n\) |

## Heap <a id="Notes"></a>



## Notes <a id="Notes"></a>

\[1\] = These operations rely on the "Amortized" part of "Amortized Worst Case". Individual actions may take surprisingly long, depending on the history of the container.

\[2\] = For these operations, the worst case _n_ is the maximum size the container ever achieved, rather than just the current size. For example, if N objects are added to a dictionary, then N-1 are deleted, the dictionary will still be sized for N objects \(at least\) until another insertion is made.

