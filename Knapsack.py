# Function to solve 0/1 Knapsack problem using dynamic programming
def knapsack_01(values, weights, capacity):
    n = len(values)
    
    # Create a 2D DP array to store the maximum value at each n-th item with weight limit w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build the DP table in a bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Include the item or exclude it
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                # Exclude the item
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

# Example usage
values = [60, 100, 120]  # Values of items
weights = [10, 20, 30]   # Weights of items
capacity = 50            # Knapsack capacity

max_value = knapsack_01(values, weights, capacity)
print(f"Maximum value in knapsack: {max_value}")
