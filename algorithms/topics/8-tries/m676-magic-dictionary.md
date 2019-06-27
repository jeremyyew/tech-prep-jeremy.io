# M676-magic-dictionary

1. **Compare by character: O\(N\*n\).**
   * Compare the input with every character in every word, and let it match wrongly once. O\(N\*n\) where N is number of words in dict, and n is number of characters in search word.
2. **Switch out letters: O\(N\)/O\(n\) \(submitted\)**
   * Build set in O\(N\) time. 
   * For each character in the search word, replace it with 25 other characters and lookup in the words dict/set. This is O\(26n\) where n is the number of characters in the search word. 
3. **Counting neighbours: O\(N\)/O\(n\).**
   * [https://leetcode.com/problems/implement-magic-dictionary/discuss/107454/Python-without-\*26-factor-in-complexity](https://leetcode.com/problems/implement-magic-dictionary/discuss/107454/Python-without-*26-factor-in-complexity)
   * O\(N\) to build, O\(n\) to search. 
4. **Trie: O\(k\) + O\(n\).**
   * Build a trie, in O\(k\) time where k is total number of characters in all dict words. 
   * If the search word already exists, then do a search that tries to swap out exactly one character. 
   * Else, traverse nodes until you reach a mismatch. At which point, recursively call `search` on all possible paths.

```python
from typing import List
import string


class MagicDictionary:
    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        self.words = set(dict)

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        for i, c in enumerate(word):
            for letter in string.ascii_letters:
                if letter == c:
                    continue
                suffix = ''
                if i < len(word) - 1:
                    suffix = word[i+1:]
                if word[:i] + letter + suffix in self.words:
                    return True
        return False


class MagicDictionaryCountingNeighbors(object):
    def _candidates(self, word):
        for i in range(len(word)):
            yield word[:i] + '*' + word[i+1:]

    def buildDict(self, words):
        self.words = set(words)
        self.near = collections.Counter(cand for word in words
                                        for cand in self._candidates(word))

    def search(self, word):
        return any(self.near[cand] > 1 or
                   self.near[cand] == 1 and word not in self.words
                   for cand in self._candidates(word))

```

