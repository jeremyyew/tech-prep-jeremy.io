'''
1. **If the prefix (l) of a word is a palindrome, then the reverse of the suffix (r) would be a potential candidate to be appended on the left to form a palindrome**. And vice-versa. 
2. This must be applied to every two-partition of each word, including empty string and the word itself. 
3. Gotcha: Words that are already palindromes will match themselves. Since there are no duplicates, there is no one else to match, so we will completely exclude this case by explicitly checking. 
4. Gotcha:To avoid duplication of full-word matches, we could choose to only append full-word matches on the left. 
'''


class Solution:
    def palindromePairs(self, words):
        def is_palindrome(check):
            return check == check[::-1]
        words = {word: i for i, word in enumerate(words)}
        pals = []
        print(words)
        for word, i in words.items():
            for j in range(len(word) + 1):  # [2]
                l, r = word[:j], word[j:]
                if (l == word and is_palindrome(l)) \
                        or (r == word and is_palindrome(r)):
                    continue  # [3]
                suffix, prefix = r[::-1], l[::-1]  # [1]
                if is_palindrome(l) and suffix in words:
                    pals.append([words[suffix], i])
                if is_palindrome(r) and prefix in words and r != '':  # [4]
                    pals.append([i, words[prefix]])
        return pals


# r = Solution().palindromePairs(
#     ["abcd", "dcba", "lls", "s", "sssll"])
# print(r)
