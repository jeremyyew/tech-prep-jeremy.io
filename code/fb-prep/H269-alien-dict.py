from collections import defaultdict


class Solution():
    def alien_dictionary(self, words):
        self.ordering = ""
        deps = defaultdict(list)
        visited = defaultdict(int)
        # construct deps
        for i in range(1, len(words)):
            w1, w2 = words[i-1], words[i]
            for j in range(min(len(w1), len(w2))):
                c1, c2 = w1[j], w2[j]
                if c1 != c2:
                    deps[c2].append(c1)

        def dfs(c):
            if visited[c] == 1:
                return
            elif visited[c] == -1:
                raise Exception("cycle found")
            visited[c] = -1
            for p in deps[c]:
                dfs(p)
            visited[c] = 1
            self.ordering += c

        for c in list(deps.keys()):
            try:
                dfs(c)
            except Exception as e:
                if str(e) == "cycle found":
                    return ""
                raise e
        return self.ordering


r = Solution().alien_dictionary(["wrt", "wrf", "er", "ett", "rftt"])
print(r)
assert(r == "wertf")


r = Solution().alien_dictionary(
    ["a", "wrt", "wrf", "er", "ett", "rftt", "z"])
print(r)
assert(r == "awertfz")


r = Solution().alien_dictionary(["z", "x"])
print(r)
assert(r == "zx")

r = Solution().alien_dictionary(["z", "x", "z"])
print(r)
assert(r == "")
