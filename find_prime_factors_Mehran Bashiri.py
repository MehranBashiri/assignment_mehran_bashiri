import time
import tracemalloc
import math
from concurrent.futures import ThreadPoolExecutor

def find_prime_factors(n):
    prime_factors = []
    
    # Handle factor of 2 separately
    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2
    
    # Handle odd factors from 3 upwards
    limit = int(math.sqrt(n)) + 1
    i = 3
    while i <= limit:
        if n % i == 0:
            prime_factors.append(i)
            while n % i == 0:
                n //= i
            limit = int(math.sqrt(n)) + 1  # Update limit as n decreases
        i += 2
    
    # If n is still greater than 2, then it is a prime number
    if n > 2:
        prime_factors.append(n)
    
    return prime_factors

def measure_performance(number):
    start_time = time.time()
    tracemalloc.start()
    
    prime_factors = find_prime_factors(number)
    
    current, peak = tracemalloc.get_traced_memory()
    end_time = time.time()
    tracemalloc.stop()
    
    print(f"Prime factors of {number}: {prime_factors}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")
    print(f"Memory usage: Current = {current / 10**6:.6f} MB; Peak = {peak / 10**6:.6f} MB\n")

def process_numbers(numbers):
    with ThreadPoolExecutor() as executor:
        executor.map(measure_performance, numbers)

# List of numbers to test, including very large primes
numbers = [1,2,1000000000039, 999999999999999999999999999999999999999999999999]

process_numbers(numbers)
