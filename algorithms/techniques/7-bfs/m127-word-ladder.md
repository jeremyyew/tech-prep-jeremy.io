# M127-word-ladder

* Construct a graph of words, with neighbors differing by one character. 
  * For every character in every `word`, replace with wildcard character \(e.g. "\*"\) to get the intermediate connecting string `s`. Add `word` to list of words that are connected by the key `s` in the dict `graph`. 
* Use a queue to BFS to get shortest path between two nodes, begin and endword. 
  * Queue instead of list gives O\(1\) popleft. 
* O\(N \* K\) to construct graph, with N number of words and K length of every word. 
* O\(N\) or O\(N^2\) for BFS? Even though BFS visits every node at most once, if we have a fully connected graph, every node still has to check that all its neighbors have been visited before skipping them. 

```python
from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        # preprocess
        graph = {}
        for word in wordList:
            for i in range(len(word)):
                s = word[:i] + "*" + word[i+1:]
                graph[s] = graph.get(s, []) + [word]
        # print(graph)

        q, visited = deque([(beginWord, 1)]), set([beginWord])
        while q:
            # print(q)
            # print(visited)
            word, steps = q.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                s = word[:i] + "*" + word[i+1:]
                nb_words = graph.get(s, [])
                for nb in nb_words:
                    if nb not in visited:
                        visited.add(nb)
                        q.append((nb, steps + 1))
        return 0


# r = Solution().ladderLength("hit", "cog",
#                             ["hot", "dot", "dog", "lot", "log", "cog"])
# print(r)

```

