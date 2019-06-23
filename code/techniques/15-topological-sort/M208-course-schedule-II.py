'''
- Use stack for topological sort; construct in reverse order, such that we only 'append' the current prerequisite once we have traversed all its children. 
- Use -1, 1, and 0 to mark unvisited, visiting, and visited, similar to M207. This is necessary since cyclical dependencies are possible. 
- Perhaps more intuitive to traverse from dependents to prereqs. 
- See https://www.geeksforgeeks.org/topological-sorting/. 
'''
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_to_course = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        stack = []
        for course, prereq in prerequisites:
            prereq_to_course[prereq].append(course)

        def traverse(prereq):
            if visited[prereq] == 1:
                return False
            elif visited[prereq] == -1:
                return True
            visited[prereq] = -1
            courses = prereq_to_course[prereq]
            for course in courses:
                cycleFound = traverse(course)
                if cycleFound:
                    return True
            visited[prereq] = 1
            stack.append(prereq)
            return False

        for prereq in range(numCourses):
            cycleFound = traverse(prereq)
            if cycleFound:
                return []
        return stack[::-1]


# r = Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
# print(r)

# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
