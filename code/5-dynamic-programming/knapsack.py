def knapSack(weights, values, capacity): 
    # number of items
    n = len(values) 
    # 2d grid
    S = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)] 

    for i in range(n + 1): 
        for c in range(capacity + 1): 
            if i == 0 or c == 0: 
                S[i][c] = 0
            elif weights[i-1] > c: 
                S[i][c] = S[i - 1][c]
            else: 
                c_prime = c - weights[i-1]
                S[i][c] = max(values[i-1] + S[i - 1][c_prime], S[i - 1][c]) 
    return S[n][capacity] 

# Driver program to test above function 
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
print(knapSack(wt, val, W)) 

