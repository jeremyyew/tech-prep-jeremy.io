'''
- By counting: `O(NK)` where `K` is the max length of string. 
    - Group all words in a dict, with the key being a count-tuple.
    - The count-tuple will be derived from an array of 26 counts (index corresponding to character), converted into a tuple so that it can be used as key. 
    - We do this instead of `Counter` because counter only has the keys it has, and isnt easily used as key of dict. 
- By sorting: `O(N * KlogK)/ O(NK)` where `K` is max length of string.  
    - Group all words in a dict, with the key being the sorted version. 
    - If we use counting sort since 26 letters, sorting = `O(K)`.


'''
import collections


class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for w in strs:
            count = [0] * 26
            for c in w:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            d[key] = d.get(key, []) + [w]
        return d.values()


class SolutionSort:
    def groupAnagrams(self, strs):
        d = {}
        for w in strs:
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()
