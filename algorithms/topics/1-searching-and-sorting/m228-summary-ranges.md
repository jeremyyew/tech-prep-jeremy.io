# M228-summary-ranges

* **Traverse: O\(N\)**. 
* **Binary search for edge of current range: O\(KlogN\) where number of ranges K &lt;= N**. 
  * \[1\] Find rightmost value at index `m` where distance between start of range and value `m - l` equals to the difference in their value.
  * \[2\] Integer division rounds down, so in base case `l = r + 1` we get `m = l`. But `diff_in_val == diff_in_index` is our inclusive condition, and that means we can't move past `m`, and we get stuck. So we need to let `m=r` since `diff_in_val > diff_in_index` is our exclusive condition.

```python
class Solution:
    def summaryRanges(self, a):
        ranges = []
        start, N = 0, len(a)
        while start < N:
            print("Start=", start)
            l, r = start, N-1
            while l < r:
                m = l + ((r - l) // 2) + 1  # [2]
                diff_in_val = a[m]-a[start]
                diff_in_index = m-start
                if diff_in_val == diff_in_index: # [1]
                    l = m
                elif diff_in_val > diff_in_index:
                    r = m-1
                else:
                    pass  # impossible
            if l > start:
                ranges.append("{}->{}".format(a[start], a[l]))
            else:
                ranges.append("{}".format(a[start]))
            start = l+1
        return ranges


# r = Solution().summaryRanges([0, 1, 2, 4, 5, 7])
# print(r)

```

