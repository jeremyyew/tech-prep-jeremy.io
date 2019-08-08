# M73-set-matrix-zeroes

* The main problem is **we can't just write zeroes iteratively since our next traversal will assume those zeroes should be expanded too.** 
* Naive: O\(MN \* M+N\) time, O\(MN\) space. 
  * Mark those to explode in empty grid. 
  * Multiple 0s in same row or cell will result in repeated traversal, hence O\(MN \* M+N\) instead of O\(MN\).
* Iteratively explode, but use marker symbol:  O\(MN \* M+N\) time, O\(1\) space. 
  * As long as not 1 or 0. 
* Keep track of rows/cols to explode in array: O\(MN\) time, O\(M + N\) space. 
* **Keep track of rows/cols to explode in first row/col of grid: O\(MN\) time, O\(1\) space.** 
  * Same as above, but traverse each cell twice only. 
  * Need a separate variable for first column/first row, since `matrix[0][0]` represents both. 
  * Otherwise any zeroes in first row will also cause all first col to have all 0s. 
  * In this solution we store `first_col` as 0 or 1. 
  * When setting the 0s, need to do in **exactly this order:**
    * Row 1, Col 1 onwards \(if we did row 0/col 0 first we overwrite the information contained, and everything becomes 0\).
    * Col 0 
    * Row 1 \(if this went before Col 0, then `matrix[0][0]` will be set\).

```python
class Solution(object):
    def setZeroes(self, matrix):
        first_col = 1
        I, J = len(matrix), len(matrix[0])
        for i in range(I):
            if matrix[i][0] == 0:
                first_col = 0
            for j in range(1, J):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1, I):
            for j in range(1, J):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(J):
                matrix[0][j] = 0

        if first_col == 0:
            for i in range(I):
                matrix[i][0] = 0

```

