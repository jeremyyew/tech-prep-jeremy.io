# Python

## What's the best way to initialize a list of known length? 

* **Use multiplication operator  `[None]  * N` in general for values/primitives.** 
* **Use list comprehension for 2d arrays/lists of objects. See below.** 
* For/While loops are the slowest, list comprehension is way faster, multiplication operator is ~6-10 times faster than list comp for N &lt; 10M.  
* [https://www.geeksforgeeks.org/python-which-is-faster-to-initialize-lists/](https://www.geeksforgeeks.org/python-which-is-faster-to-initialize-lists/)

{% hint style="info" %}
Multiplication operator uses reference aka shallow copies:

> ...replicating a list with `*` doesn’t create copies, it only creates references to the existing objects. The `* 3` in `A = [[None]*2] * 3` creates a list containing 3 references to the same list of length two. Changes to one row will show in all rows...
>
> The suggested approach is to create a list of the desired length first and then fill in each element with a newly created list...You can also use a list comprehension: A = \[\[None\] \* 2 for i in range\(3\)\]

[https://docs.python.org/2/faq/programming.html\#how-do-i-create-a-multidimensional-list: ](https://docs.python.org/2/faq/programming.html#how-do-i-create-a-multidimensional-list:%20)
{% endhint %}

## Shallow vs Deep copying

* [https://www.python-course.eu/python3\_deep\_copy.php](https://www.python-course.eu/python3_deep_copy.php)

## When are function parameters pass-by-reference and pass-by-value?

## Should we use enumerate or range for loops?

Use `enumerate`. It is faster and cleaner. [https://dbader.org/blog/python-enumerate](https://dbader.org/blog/python-enumerate) 

## How does Python deal with recursion? 

Default 1000 level stack limit, otherwise stack overflow. No tail-call optimization either. See [https://stackoverflow.com/questions/13591970/does-python-optimize-tail-recursion](https://stackoverflow.com/questions/13591970/does-python-optimize-tail-recursion). 

## How do we filter with list comprehension? 

Instead of getting default values:

```python
even = [n if n % 2 else None for n in [1, 2, 3, 4]]
# [None, 2, None, 4]
```

Try filtering with a conditional: 

```python
even = [n for n in [1, 2, 3, 4] if n % 2]
# [2, 4]
```

Remember, now you may get an empty list! So if you are passing the comprehended list to an operation that requires a non-empty sequence, say `min`  or `max`, remember to add a default non-empty list that gives the default value: 

```python
smallest_even = min([n for n in [1, 3, 5, 7] if n % 2] or [0])
```

















