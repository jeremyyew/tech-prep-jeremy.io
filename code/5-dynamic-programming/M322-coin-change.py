
'''
Let num(v) be the number of coins needed to form value v, and let C = {c_1, c_2...c_n} be the set of coin values. Then, 

[1] num(v) = min{num(v - c) for all c <= v in C} + 1. 
[2] num(0) = 0. 
[3] We use the base case 0 to express the other base cases (where c = v). 
[4] Remember to only subtract c <= v. Since we are doing list comprehension, we have to return some num for every c, even when c > v, so we use inf since we cant min on None. 


As it turns out, for this problem, recursive version is an absolute no, even with LRU cache, due to exponential branching on large N.  

1. Iterative version
Decent speed. Always N iterations, which is a good thing in . Only slower than [2] and [3] on nice inputs. 

2. Recursive version with self-written memoize
MUST memoize, otherwise lots of overlap. It may be less calls depending on input, e.g. n=100 and coins == [10] (we jump to 0 in 10 calls). But takes too long on large N with weird coins. 


3. Recursive version with LRU cache
Also takes too long on large N with weird coins. 

'''
import math
from typing import List
import functools
import timeit


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        num = [None for _ in range(amount+1)]
        num[0] = 0  # [3]
        for v in range(1, amount+1):
            # print(v)
            num[v] = min(
                [num[v-c] if c <= v else math.inf for c in coins]) + 1  # [1], [4]
        return num[amount] if num[amount] != math.inf else -1


class SolutionRecLRU:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        num = self.coinChangeRec(amount)
        return num if num != math.inf else -1

    @functools.lru_cache()
    def coinChangeRec(self, v: int) -> int:
        print(v)
        if v == 0:
            return 0
        return min([self.coinChangeRec(v-c) if c <=
                    v else math.inf for c in self.coins]) + 1


def memoize(func):
    '''
A simple memoize from scratch, with unbounded storage. 
- Always use built-in cache, faster and more options.  
- Unbounded storage not good. 
- If writing your own decorator remember to put @functools.wraps(func), this will allow the decorated fn to retain its identity. 
'''
    cache = dict()

    @functools.wraps(func)
    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return memoized_func


class SolutionRec:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        num = self.coinChangeRec(amount)
        return num if num != math.inf else -1

    @memoize
    def coinChangeRec(self, v: int) -> int:
        # print(v)
        if v == 0:
            return 0
        return min([self.coinChangeRec(v-c) if c <=
                    v else math.inf for c in self.coins]) + 1


# print(Solution().coinChange([186, 419, 83, 408], 6249))

# print(timeit.timeit(
#     'SolutionIter().coinChange([1, 2, 5], 100)', globals=globals(), number=1))
# print(timeit.timeit(
#     'SolutionRec().coinChange([1, 2, 5], 100)', globals=globals(), number=1))
# print(timeit.timeit(
#     'Solution().coinChange([1, 2, 5], 100)', globals=globals(), number=1))
