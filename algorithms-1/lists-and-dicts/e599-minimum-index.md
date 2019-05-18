# E599-minimum-index

```python
class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        sums = {}
        minm = len(list1) + len(list2)
        res = []
        for i in range(len(list1)):
            sums[list1[i]] = i
        for i in range(len(list2)):
            if list2[i] in sums:
                summ = sums[list2[i]] + i
                if summ == minm:
                    res.append(list2[i])
                elif summ < minm:
                    res = [list2[i]]
                    minm = summ
        return res

s = Solution()
print(s.findRestaurant(["a", "b", "d"], ["e", "b", "a"]))
print(s.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],
["KFC","Shogun","Burger King"]))

```

