# M442-find-all-duplicates-in-an-array

* We could sort but that gives &gt; O\(N\) runtime. 
* We could do bin sort but that requires O\(N\) space. 
* We can collect values in a dict/set but that also requires O\(N\) space. 
* We could follow the cyclic-sort pattern of shifting values to their indices, and recording somewhere whenever we see a duplicate.
  * Once we see a duplicate, we need to mark the original value somehow so we know it has been accounted for, otherwise we may later try to displace it again. 
  * But then the first value will be swapped out without a replacement, and then we need some special case, and it gets complicated. 
* So perhaps, instead of doing a chain of displacements, we could simply mark the value at the index \(say, as negative\) to signify we have seen the value of the index. 
  * This way, we don't need to cycle through displacements; we retain the information of that value so that later on we can still place it properly it. 
  * Essentially we are using the array itself as a set. 

```python
class Solution:
   def findDuplicates(self, nums):
       ans = []
       for n in nums:
           ind = abs(n) - 1
           if nums[ind] < 0:
               ans.append(abs(n))
           nums[ind] = - nums[ind]

       return ans
```

