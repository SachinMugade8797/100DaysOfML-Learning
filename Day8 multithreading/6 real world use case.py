

import multiprocessing
import math
import sys
import time

# Increasing the maximum number of digits for integer conversion
# This is set in the system library to handle large factorial calculations.
sys.set_int_max_str_digits(100000)

# Function to compute factorial of a given number
def compute_factorial(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is computed")
    return result

if __name__ == "__main__":
    # List of numbers for which factorial will be calculated
    numbers = [1,2,3,4,5]

    # Start timer
    start_time = time.time()

    # Create a pool of worker processes
    with multiprocessing.Pool() as pool:
        # Map the compute_factorial function to all numbers in the list
        results = pool.map(compute_factorial, numbers)

    # End timer
    end_time = time.time()

    # Print the calculated results and the time taken
    print(f"Results: {results}")

    print(f"Time taken: {end_time - start_time} seconds")
