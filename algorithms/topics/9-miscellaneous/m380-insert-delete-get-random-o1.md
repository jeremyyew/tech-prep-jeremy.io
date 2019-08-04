# M380-insert-delete-get-random-o1

* **With set**:
  * O\(1\) membership check, insert and remove \(assuming no hash collisions, otherwise O\(N\) for membership check, and insert and remove too since they have to check\). 
  * For `getRandom`, we could use `pop` \(and then push back\) which returns an arbitrary element, or `next(iter(S))` which is also arbitrary. But perhaps not truly random? 
  * Same applies to dict keys, they are implemented similarly.
* **Without using set \(dict + list\)**:
  * Dict lets us check membership, add and remove in O\(1\). 
  * List allows us to randomly pick a member by randomly generating index, for `getRandom`. List is also O\(1\) to add. 
    * **To remove in O\(1\), we overwrite the item to be deleted with the last element, and delete the last element - O\(1\) as no shifting**. 
    * To achieve this, we therefore store pointers \(indexes\) to elements in the list as values in the dict. Then we simply have to update the index of that last element. 
  * Also assumes **no hash collisions**.

```python

import random


class RandomizedSet(object):

    def __init__(self):
        self.nums, self.pos = [], {}

    def insert(self, val):
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val):
        if val in self.pos:
            idx, last = self.pos[val], self.nums[-1]
            self.nums[idx], self.pos[last] = last, idx
            self.nums.pop()
            self.pos.pop(val, 0)
            return True
        return False

    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]

```

