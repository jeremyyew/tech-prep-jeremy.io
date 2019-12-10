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


r = Solution().ladderLength("hit", "cog",
                            ["hot", "dot", "dog", "lot", "log", "cog"])
print(r)
