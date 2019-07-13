# M621-task-scheduler

1. **Total intervals = idle intervals + total tasks.**
2. There is a minimum number of cycles, which is max value of reps minus 1, i.e. `cycles = reps[0] - 1`.
3. For every other task, we replace an idle slot, therefore we subtract that number of idle intervals. 
4. In the special case where we have a task `rep` equal to max value rep, we only minus `cycle` \(max value -1\). Since we are only filling up `cycle` number of idle intervals, the last extra task will be put beside the last non-idle cycle \(see diagram\). Therefore, we subtract `idle -= min(rep, cycle)`. 
5. In the case where `idle` is negative \(there are enough distinct tasks such that there were no idle slots\), the answer is simply `len(tasks)`. Therefore we return`min(0, idle) + len(tasks)`.

See [https://leetcode.com/articles/task-scheduler/](https://leetcode.com/articles/task-scheduler/), solution 3.

```python
from collections import Counter

class Solution:
    def leastInterval(self, tasks, n) -> int:
        if n == 0:
            return len(tasks)
        task_counts = Counter(tasks)
        reps = sorted(task_counts.values(), reverse=True)
        # [2]
        cycles = reps[0] - 1
        idle = cycles * n
        for rep in reps[1:]:
            idle -= min(rep, cycles)  # [3], [4]
        return len(tasks) + min(0, idle)  # [1], [5]

```

