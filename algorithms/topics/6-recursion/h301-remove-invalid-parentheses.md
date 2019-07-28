# H301-remove-invalid-parentheses

* Brute force: At every step we can keep or leave. While traversing we keep track of number of invalid parens. O\(2^N\).
* **All max-length valid expressions will have the same length.**
  * **So if we get min num of removals `k` first, we only have to do `N-choose-k` combinations.** We limit the number of removals. 
  * In one pass: count number of misplaced left and right parens.
  * Then, simply traverse the string, accumulating potential answers. You get to try an alternate traversal by skipping a character, only if you still have removals left. 
* **Worst case all elements can be removable, each step has two options, so O\(2^N\) still.**
* Note: We must remove duplicates, because we want only unique sequences, not all traversals, and multiple valid traversals can result in the same sequence.
* Other optimizations: 
  * We can keep track not just of total characters to be removed, but specifically number of left and right chars to be removed, `rmL` and  `rmR`. 
  * Keep track of left and right parens left in the string, so we can always immediately tell if there is no change of a valid string any longer. 
  * Instead of index string repeatedly, just add the literal char. 

```python
from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        l = r = 0
        for p in s:
            if p == '(':
                l += 1
            if p == ')':
                if l > 0:
                    l -= 1
                else:
                    r += 1

        def traverse(seq, i, l, r, rmL, rmR):
            # print(f"seq={seq}, s={s}, l={l}, r={r}, rm={rm}")
            if i == len(s):
                if l == 0 and r == 0:
                    # print(f"adding: {seq}")
                    self.valid_sequences.add(seq)
            elif s[i] == '(':
                traverse(seq + '(', i+1, l+1, r, rmL, rmR)
                if rmL > 0:
                    traverse(seq, i+1, l, r, rmL-1, rmR)
            elif s[i] == ')':
                if l > 0:
                    traverse(seq + ')', i+1, l-1, r, rmL, rmR)
                else:
                    traverse(seq, i+1, l, r+1, rmL, rmR)
                if rmR > 0:
                    traverse(seq, i+1, l, r, rmL, rmR - 1)
            else:
                traverse(seq + s[i], i+1, l, r, rmL, rmR)

        self.valid_sequences = set()
        traverse('', 0, 0, 0, l, r)
        return self.valid_sequences

```

