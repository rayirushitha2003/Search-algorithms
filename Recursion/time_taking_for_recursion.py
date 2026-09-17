import time

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


values = [10, 20, 30, 40, 50]

for n in values:
    start = time.time()
    
    result = fib(n)
    
    end = time.time()
    
    print(f"fib({n}) = {result}, Time = {end - start:.5f} seconds")