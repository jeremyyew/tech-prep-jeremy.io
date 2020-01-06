# M210-course-schedule-II

* Satisfy all dependencies before adding the current node. 
* Use -1, 1, and 0 to mark unvisited, visiting, and visited, similar to M207. 
* Raise an exception if there is a cycle. 
* Perhaps more intuitive to traverse from dependents to prereqs. 
* See [https://www.geeksforgeeks.org/topological-sorting/](https://www.geeksforgeeks.org/topological-sorting/). 

```python
from typing import List
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        c_to_p = defaultdict(list)
        visited = defaultdict(int)
        order = []
        for c, p in prerequisites:
            c_to_p[c].append(p)

        def satisfy_p(c):
            if visited[c] == 1:
                return
            elif visited[c] == -1:
                raise Exception("cycle found")
            visited[c] = -1
            for p in c_to_p[c]:
                satisfy_p(p)
            visited[c] = 1
            order.append(c)

        for c in range(numCourses):
            try:
                satisfy_p(c)
            except Exception as e:
                if str(e) == "cycle found":
                    return []
                raise e
        return order


r = Solution().findOrder(2, [[1, 0]])
print(r)
```

