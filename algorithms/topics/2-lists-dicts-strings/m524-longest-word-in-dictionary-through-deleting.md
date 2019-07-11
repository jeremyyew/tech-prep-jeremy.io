# M524-longest-word-in-dictionary-through-deleting

* Sort by word length first and then by alphabetical order. 
* Otherwise it will be by alphabetical, with shorter words appearing after longer words because their letter is later. 
* Descending order of length. 
* Sorting helps us stop once we find a 'best' solution. But increases time complexity. 

1. With Sorting
   * O\(\(n_x\)logn+ n_x\) time. Sorting over x-length strings, and checking n of x-length strings for subsequences. 
   * O\(logn\) space from sorting. 
2. Without Sorting
   * O\(n \* x\) time, where x is average str length. 
   * O\(x\) space. 

See [https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/discuss/99583/Python-Simple-\(Two-pointer](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/discuss/99583/Python-Simple-%28Two-pointer)\)

```python

def findLongestWord(self, S, D):
    D.sort(key = lambda x: (-len(x), x))
    for word in D:
        i = 0
        for c in S:
            if i < len(word) and word[i] == c:
                i += 1
        if i == len(word):
            return word
    return ""
```

