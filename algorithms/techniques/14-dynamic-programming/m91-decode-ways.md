# M91-decode-ways

### Summary 

We basically have to make two checks:

1. If the **next** character forms a **valid single-digit value,** and can thus be **appended as itself** to every decoding of the **previous substring.** 
2. If the **next and previous** character form **a valid double-digit value,** and can thus be **appended as a pair** to every decoding of the **second-to-last substring.** 

Formally \(without the base cases\): 

```text
if s[i-1] != '0':
    dp[i] += dp[i-1]
if "09" < s[i-2:i] < "27":
    dp[i] += dp[i-2]
```

### Walkthrough: 

* Base case, `i == 1`: 
  * if `s[0] == "0"`: 
    * no letters match, so `dp[1] = 0`.
  * else `s[0] != "0"`:
    * 1 way to match, `dp[1] = 1`.
* Induction case, `i > 1`: 
  * Let `s'` be one possible decoding of `s[0:i-1]`, the previous substring. Then, for the next character `s[i-1]`:
  * if `s[i-1] == '0'`: 
    * we cant form `s'|0` since `0` is invalid, so add nothing. 
    * `dp[i] == 0`
  * else `s[i-1] != '0'`:
    * we can form `s'|s[i-1]` for each `s'`, so add `|s'| = dp[i-1]`.
    * `dp[i] == dp[i-1]`
  * Let `s''` be one possible decoding of `s[0:i-2]`, the second-last substring. 
  * Now let's see what value the last character `s[i-2]` paired with our next character `s[i-1]` would form.  
  * if `"09" < s[i-2:i] < "27"`:
    * we can form `s''|s[i-2:i]`, so also add `|s''| = dp[i-2]`.
    * `dp[i] += dp[i-2]`.
  * else: 
    * we cant form `s''|s[i-2:i]`, since `s[i-2:i]` is invalid, so pass. 

Example:

* s = "22160"
  * "" -&gt; "" 
    * `1` \(but return base case `0`\)
  * `"2"` 
    * -&gt; `"2"` 
    * base case `1`
  * `"22"` 
    * -&gt; `"2|2", "22"` 
    * "2" and "22" are valid so `1 + 1 -> 2`
  * `"221"` 
    * -&gt; `"2|2|1",   "22|1",   "2|21"` 
    * "1" and "21" are valid so `2 + 1 -> 3`
  * `"2216"` 
    * -&gt; `"2|2|1|6", "22|1|6", "2|21|6", "2|2|16", "22|16"` 
    * "6" and "16" are valid so `2 + 3 -> 5`
  * `"22160"` 
    * -&gt; `"2|2|1|6", "22|1|6", "2|21|6"`
    * "0" and "60" are NOT valid so `0`. We can't actually form any sequences. 

```python

class Solution:
    def numDecodings(self, s: str) -> int:
        if s == "":
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if i != 1 and s[i-2:i] < "27" and s[i-2:i] > "09":
                dp[i] += dp[i-2]
        return dp[n]

```

