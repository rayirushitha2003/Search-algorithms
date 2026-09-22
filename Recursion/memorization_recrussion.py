from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fibonacci(number):
    """
    Calculate the nth Fibonacci number using recursion + memoization.

    Parameters:
    number (int): Position in Fibonacci sequence

    Returns:
    int: Fibonacci value at position 'number'
    """

    # ✅ Input validation
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")

    if number < 0:
        raise ValueError("Input must be non-negative")

    # ✅ Base cases
    if number <= 1:
        return number

    # ✅ Recursive case with memoization (handled by lru_cache)
    return fibonacci(number - 1) + fibonacci(number - 2)


def measure_time(n):
    """
    Measure execution time for fibonacci calculation.
    """
    start_time = time.time()

    try:
        result = fibonacci(n)
        end_time = time.time()

        print(f"Fibonacci({n}) = {result}")
        print(f"Time taken = {end_time - start_time:.6f} seconds")

    except ValueError as error:
        print("Error:", error)


# ✅ Test cases
test_values = [10, 20, 30, 40, 50]

for value in test_values:
    print("\n--- Testing for n =", value, "---")
    measure_time(value)