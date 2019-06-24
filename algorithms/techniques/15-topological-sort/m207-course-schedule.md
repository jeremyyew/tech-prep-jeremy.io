# M207-course-schedule

* Mark all nodes `0` to represent not visited, 
* If `visited[v]=0`, this is an unvisited node, so mark `-1`, i.e. visited on this path. 
* Then, recursively check all ancestors. Once we have verified that none of the ancestors of this node are part of a cycle, then this node is not part of a cycle. So mark as `1` and return False. 
* If `visited[v]=-1`, we recently visited node `v` on the current path, so it is part of a cycle, so return `True`. 
* Else if `visited[v]=1`, we have already verified that it is not part of a cycle, so return False. This prevents us from traversing nodes repeatedly and incurring possibly `O(V!)` time.  

```python
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for v, p in prerequisites:
            prereqs[v].append(p)

        def partOfCycle(v):
            if visited[v] == -1:
                return True
            elif visited[v] == 1:
                return False
            visited[v] = -1
            for p in prereqs[v]:
                if partOfCycle(p):
                    return True
            visited[v] = 1
            return False

        for v in range(numCourses):
            if partOfCycle(v):
                return False
        return True


# r = Solution().canFinish(2, [[0, 1], [1, 0]])
# print(r)

```

