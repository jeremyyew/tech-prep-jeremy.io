# E121-buy-sell-stock

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # keep track of max profit so far
        # maxProfitNew = max(maxProfit, currentPrice - lowestPrice)
        # keep track of lowestPrice so far too 
        maxProfit = 0
        lowestPrice = None
        for price in prices: 
            if lowestPrice is None: 
                lowestPrice = price
                continue
            maxProfit = max(maxProfit, price - lowestPrice)
            lowestPrice = min(lowestPrice, price)
        return maxProfit
```

