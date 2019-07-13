'''
- Total intervals = idle intervals + total tasks
- There is a min number of cycles, which is max value of reps minus 1. 
- For every other task, we replace that number of idle intervals.
- In the special case where we have a task rep = max value, we only minus `cycle` (max value -1), since we are only filling up `cycle` number of idle intervals, the last extra task will be put beside the last non-idle cycle (see diagram).
See https://leetcode.com/articles/task-scheduler/ solution 3. 
'''
from collections import Counter


class Solution:
    def leastInterval(self, tasks, n) -> int:
        if n == 0:
            return len(tasks)
        task_counts = Counter(tasks)
        reps = sorted(task_counts.values(), reverse=True)
        # Min num of cycles needed based on max-rep task.
        cycles = reps[0] - 1
        idle = cycles * n
        for rep in reps[1:]:
             # We have to get min because for rep = max_value, (i.e rep = cycles + 1), we only minus rep; the last task will be put beside the last non-idle cycle (see diagram).
            idle -= min(rep, cycles)
        return idle + len(tasks) if idle > 0 else len(tasks)
