# M208-course-schedule-II

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
        course_to_prereqs = defaultdict(list)
        visited = defaultdict(int)
        for c, p in prerequisites:
            course_to_prereqs[c].append(p)

        order = []

        def satisfy_prereqs(c):
            if visited[c] == 1:
                return
            elif visited[c] == -1:
                raise Exception("CycleFound")
            visited[c] = -1
            for p in course_to_prereqs[c]:
                satisfy_prereqs(p)
            visited[c] = 1
            order.append(c)
            # print(order)

        for course in range(numCourses):
            try:
                satisfy_prereqs(course)
            except Exception as e:
                if str(e) == ("CycleFound"):
                    # print("except")
                    return []
                raise e
        return order


# r = Solution().findOrder(2, [[1, 0]])
# print(r)

```

