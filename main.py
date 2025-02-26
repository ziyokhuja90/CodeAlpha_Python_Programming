"""
FIBONACCI GENERATOR

The Fibonacci series is a sequence where each number is
the sum of the two preceding numbers, defined by a
mathematical recurrence relationship.
"""

def fib(n: int) -> int:
    if n == 1:  # Handle the first Fibonacci number
        return 1

    left, right = 0, 1  # Start with the first two numbers
    count = 1  # Track the current position

    while count <= n:  # Loop until we reach the nth number
        next_number = left + right  # Calculate the next number
        left = right  # Move to the next pair
        right = next_number
        count += 1  # Increment the position

    return left  # Return the nth Fibonacci number

print(fib(3))