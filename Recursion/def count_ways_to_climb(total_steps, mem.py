def count_ways_to_climb(total_steps, memo=None):
    """
    Calculates the number of distinct ways to climb a staircase.

    You can climb either 1 step or 2 steps at a time.

    Parameters:
        total_steps (int): Total number of steps in the staircase
        memo (dict): Dictionary used for memoization (caching results)

    Returns:
        int: Number of distinct ways to reach the top

    Raises:
        ValueError: If total_steps is negative
        TypeError: If total_steps is not an integer
    """

    # ---------- Input Validation ----------
    if not isinstance(total_steps, int):
        raise TypeError("Number of steps must be an integer")

    if total_steps < 0:
        raise ValueError("Number of steps cannot be negative")

    # Initialize memo dictionary only once
    if memo is None:
        memo = {}

    # ---------- Base Cases ----------
    if total_steps == 0:
        return 1  # One way: do nothing
    if total_steps == 1:
        return 1  # Only one step possible

    # ---------- Check Cached Result ----------
    if total_steps in memo:
        return memo[total_steps]

    # ---------- Recursive Computation ----------
    ways_from_previous_step = count_ways_to_climb(total_steps - 1, memo)
    ways_from_two_steps_before = count_ways_to_climb(total_steps - 2, memo)

    total_ways = ways_from_previous_step + ways_from_two_steps_before

    # Store result in cache
    memo[total_steps] = total_ways

    return total_ways


# ---------- Main Execution ----------
if __name__ == "__main__":
    try:
        steps = 5
        result = count_ways_to_climb(steps)
        print(f"Number of ways to climb {steps} steps: {result}")
    except Exception as error:
        print(f"Error: {error}")