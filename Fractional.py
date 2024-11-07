# Function to solve fractional knapsack problem
def fractional_knapsack(values, weights, capacity):
    # Calculate value-to-weight ratio for each item and store it with value and weight
    items = [(values[i] / weights[i], values[i], weights[i]) for i in range(len(values))]
    # Sort items by value-to-weight ratio in descending order
    items.sort(reverse=True, key=lambda x: x[0])

    total_value = 0.0  # Total value of knapsack
    for ratio, value, weight in items:
        if capacity > 0 and weight <= capacity:
            # If the item can be fully taken, take it
            capacity -= weight
            total_value += value
        else:
            # Take fraction of the item if it can't be fully taken
            total_value += ratio * capacity
            break

    return total_value

# Example usage
values = [60, 100, 120]  # Values of items
weights = [10, 20, 30]   # Weights of items
capacity = 50            # Knapsack capacity

max_value = fractional_knapsack(values, weights, capacity)
print(f"Maximum value in knapsack: {max_value}")
