'''
If `word[i] == '.'`, then return the result of a search from each existing child, beginning from `word[i+1]`, as if that was the correct child. 
'''


class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False

    def contains(self, child):
        return self.children[child] is not None

    def charToChildKey(self, ch):
        return ord(ch)-ord('a')

    def getAllChildren(self):
        return [child for child in self.children if child]


class WordDictionary:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            k = node.charToChildKey(c)
            if not node.contains(k):
                node.children[k] = self.getNode()
            node = node.children[k]
        node.isEnd = True

    def search(self, word: str) -> bool:
        return self.searchRec(word, self.root)

    def searchRec(self, word: str, node: TrieNode) -> bool:
        for i in range(len(word)):
            if word[i] == '.':
                for child in node.getAllChildren():
                    if self.searchRec(word[i+1:], child):
                        return True
                return False
            else:
                k = node.charToChildKey(word[i])
                if not node.contains(k):
                    return False
                node = node.children[k]
        return node.isEnd


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
