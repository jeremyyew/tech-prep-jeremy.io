'''
- Store paths instead of path length. It does seem like a lot of space, but even if you use pointers its the same amount of space.  
- Once there is a min path, terminate any other path that is the same length. 
- Do not use a global visited - we need all paths, including paths that use the same nodes. Instead, check if the next node is in the current path.
- Reduce complexity of checking membership in path, with an additional path_set.
- We must copy path_set for each neighbor, otherwise the path_set gets modified repeatedly. 
'''
from typing import List
from collections import deque


class Solution(object):
    def findLadders(self, beginWord: str, endWord: str,
                    wordList: List[str]) -> List[List[str]]:
        # preprocess
        g = {}
        for word in wordList:
            for i in range(len(word)):
                s = word[:i] + "*" + word[i+1:]
                g[s] = g.get(s, []) + [word]
        # bfs
        q = deque([([beginWord], set([beginWord]))])
        paths = []
        while q:
            # print(q)
            # print(paths)
            path, path_set = q.popleft()
            if paths and len(path) == len(paths[0]):
                continue
            word = path[-1]
            for i in range(len(word)):
                s = word[:i] + "*" + word[i+1:]
                nbs = g.get(s, [])
                for nb in nbs:
                    if nb == endWord:
                        paths.append(path + [nb])
                    elif nb not in path_set:
                        pcopy = path_set.copy()
                        pcopy.add(nb)
                        q.append((path + [nb], pcopy))
        return paths


# r = Solution().findLadders("hit", "cog",
#                            ["hot", "dot", "dog", "lot", "log", "cog"])
# print(r)
# Output:
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]
r = Solution().findLadders("red", "tax",
                           ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"])
print(r)
# [["red","ted","tad","tax"],["red","ted","tex","tax"],["red","rex","tex","tax"]]
