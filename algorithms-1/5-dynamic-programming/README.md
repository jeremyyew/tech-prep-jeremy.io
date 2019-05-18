# 5. Dynamic Programming

**From** [**https://dev.to/nikolaotasevic/dynamic-programming--7-steps-to-solve-any-dp-interview-problem-3870**](https://dev.to/nikolaotasevic/dynamic-programming--7-steps-to-solve-any-dp-interview-problem-3870)**.** 

1. **Identify DP: Can we obtain a solution using solutions to subproblems?** 
2. **Identify problem variables.** 
3. **Express the recurrence relation:**  
   1. How would you combine subproblem solutions to attain a main solution? 
4. **Identify the base cases:** 
   1. What cases have an obvious solution? 
   2. What are illegal values for parameters? 
   3. What conditions can we use to catch these base cases? 
   4. Do we need to worry about 'jumping past' the base case with illegal values? 
5. **Iterative or recursive**
   1. Big O time complexity is same. 
   2. Usually recursive is easier to reason about, since for iterative we need to figure out what values we need and the order in which to compute. 
   3. Recursive potentially faster depending on the input. 
   4. Furthermore we can speed up recursive programs with memoization. 
   5. However there might be a stack limit. 
6. **Add memoization**
7. **Determine time complexity**

![](../../.gitbook/assets/image%20%281%29.png)

