# Recursive function to calculate Fibonacci numbers with step count
def fibonacci_recursive(n, step_counter):
    # Increment step count
    step_counter[0] += 1

    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive call
        return fibonacci_recursive(n - 1, step_counter) + fibonacci_recursive(n - 2, step_counter)

# Driver code
n = int(input("Enter the value of n: "))
step_counter = [0]  # Using a list to keep count of steps as a mutable object
result = fibonacci_recursive(n, step_counter)
print(f"Fibonacci({n}) = {result}")
print(f"Steps taken (recursive approach): {step_counter[0]}")


# Iterative function to calculate Fibonacci numbers with step count
def fibonacci_iterative(n):
    step_count = 0

    # Base cases
    if n <= 0:
        return 0, step_count
    elif n == 1:
        return 1, step_count + 1

    # Iterative calculation
    a, b = 0, 1
    for _ in range(2, n + 1):
        step_count += 1
        a, b = b, a + b

    return b, step_count

# Driver code
n = int(input("Enter the value of n: "))
result, step_count = fibonacci_iterative(n)
print(f"Fibonacci({n}) = {result}")
print(f"Steps taken (iterative approach): {step_count}")
