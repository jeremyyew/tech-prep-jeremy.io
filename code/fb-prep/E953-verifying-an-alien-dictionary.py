from typing import List


class Solution:
    def isAlienSortedNlogN(self, words: List[str], order: str) -> bool:
        mapping = {}
        human_order = "abcdefghijklmnopqrstuvqxyz"
        for x, y in zip(order, human_order):
            mapping[x] = y
        if words != sorted(
                words,
                key=lambda w: "".join([mapping[c] for c in w])):
            return False
        return True

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Linear time.
        mapping = {}
        human_order = "abcdefghijklmnopqrstuvqxyz"
        for x, y in zip(order, human_order):
            mapping[x] = y
        human_words = ["".join([mapping[c] for c in w]) for w in words]
        for i in range(1, len(human_words)):
            if human_words[i-1] > human_words[i]:
                return False
        return True


r = Solution().isAlienSorted(
    ["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz")
assert(r)
r = Solution().isAlienSorted(
    ["word", "world", "row"], "worldabcefghijkmnpqstuvxyz")
assert(not r)
r = Solution().isAlienSorted(
    ["apple", "app"], "abcdefghijklmnopqrstuvwxyz")
assert(not r)
