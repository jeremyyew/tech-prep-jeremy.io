'''
Here we implement a simple trie data structure that allows you to:
- insert a word into the trie;
- search if a word is in the trie; 
- search if any words with a prefix is in the trie. 

There are two underlying node implementations provided: 
- `TrieNodeWithArray` stores child keys as an array of length 26 (and is meant to be mapped specifically to the 26 lowercase characters)
- `TrieNodeWithDict` stores child keys in a dict, so it should work for any legal string, since it maps any char into its corresponding Unicode code point. https://docs.python.org/2/library/functions.html#ord
- Each has its own `contains` and `charToChildKey` methods so that similar code can work with both.  

Adapted from:
- https://www.geeksforgeeks.org/trie-insert-and-search/, code by Atul Kumar (www.facebook.com/atul.kr.007) 
- https://leetcode.com/problems/implement-trie-prefix-tree/solution/. 
'''


class TrieNodeWithDict:
    def __init__(self):
        self.children = {}
        self.isEnd = False

    def contains(self, child):
        return child in self.children

    def charToChildKey(self, ch):
        return ord(ch)


class TrieNodeWithArray:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False

    def contains(self, child):
        return self.children[child] is not None

    def charToChildKey(self, ch):
        return ord(ch)-ord('a')


class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNodeWithDict()
        # return TrieNodeWithArray()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            k = node.charToChildKey(c)
            if not node.contains(k):
                node.children[k] = self.getNode()
            node = node.children[k]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.findPrefix(word)
        return node != None and node.isEnd

    def findPrefix(self, word: str) -> TrieNodeWithArray:
        node = self.root
        for c in word:
            k = node.charToChildKey(c)
            if not node.contains(k):
                return None
            node = node.children[k]
        return node

    def startsWith(self, prefix: str) -> bool:
        node = self.findPrefix(prefix)
        return node != None

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
