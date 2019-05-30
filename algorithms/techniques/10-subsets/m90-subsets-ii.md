# M90-subsets-II

{% hint style="info" %}
**Instead of adding the duplicate all the existing subsets, only add it to the subsets which were created in the previous step**.
{% endhint %}

1. Solution with `prev_added` variable. 
2. Solution with indexing to get previously added subset elements. 

Since the given set can have duplicate numbers, if we follow the same approach discussed in Subsets, we will end up with duplicate subsets, which is not acceptable. To handle this, we will do two extra things:

1. Sort all numbers of the given set. This will ensure that all duplicate numbers are next to each other.
2. Follow the same BFS approach but whenever we are about to process a duplicate \(i.e., when the current and the previous numbers are same\), **instead of adding the current number \(which is a duplicate\) to all the existing subsets, only add it to the subsets which were created in the previous step**.

Example: Given set: `[1, 5, 3, 3]`. Sorted set: `[1, 3, 3, 5]`.

1. Start with an empty set: `[[]]`.  
2. Add the first number \(1\) to all the existing subsets to create new subsets: `[[], [1]]`.  
3. Add the second number \(3\) to all the existing subsets: `[[], [1], [3], [1,3]]`.
4. The next number \(3\) is a duplicate. If we add it to all existing subsets we will get:  

    `[[], [1], [3], [1,3], [3], [1,3], [3,3], [1,3,3]]`.  

    We got two duplicate subsets: `[3], [1,3]`.  

    Whereas we only needed the new subsets: `[3,3], [1,3,3]`. 

5. To handle this instead of adding \(3\) to all the existing subsets, we only add it to the new subsets which were created in the previous \(3rd\) step:  

    `[[], [1], [3], [1,3], [3,3], [1,3,3]]`.  

6. Finally, add the forth number \(5\) to all the existing subsets:  

    `[[], [1], [3], [1,3], [3,3], [1,3,3], [5], [1,5], [3,5], [1,3,5], [3,3,5], [1,3,3,5]]`. 

```python

class Solution():
    def subsetsWithDup(self, nums):
        nums.sort()
        prev_added, subsets = [], [[]]
        for i in range(len(nums)):
            dup = i > 0 and nums[i] == nums[i-1]
            to_add = [subset + [nums[i]]
                      for subset in (prev_added
                                     if (dup) else
                                     subsets)]
            subsets = subsets + to_add
            prev_added = to_add
        return subsets


class SolutionIndexing():
    def subsetsWithDup(self, nums):
        nums.sort()
        subsets = [[]]
        startIndex, endIndex = 0, 0
        for i in range(len(nums)):
            startIndex = 0
            if i > 0 and nums[i] == nums[i - 1]:
                startIndex = endIndex + 1
            endIndex = len(subsets) - 1
            for j in range(startIndex, endIndex+1):
                set = list(subsets[j])
                set.append(nums[i])
                subsets.append(set)
        return subsets

```

