'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true

Note:
You may assume both s and t have the same length.
'''

'''
For each new pair of characters s_i and t_i,  we register their one-to-one mapping via a key-value entry s_i: t_i in a dictionary. 
If we have an existing s_i, t_i should match, else we have one s_i mapped to two different t_i. 
If we a new s_i, then t_i must also be new, else we have two different s_i mapped to one t_i. 
FYI its faster to zip than index two arrays. 
'''

import collections


class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: tr
        :rtype: bool
        """
        mappings = {}
        for s_i, t_i in zip(s, t):
            if s_i in mappings and mappings[s_i] != t_i:
                return False
            elif s_i not in mappings and t_i in mappings.values():
                return False
            else:
                mappings[s_i] = t_i
        return True
