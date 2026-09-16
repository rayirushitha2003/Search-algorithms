def gcd(a, b):
    if b == 0:        # Base condition
        return a
    return gcd(b, a % b)   # Recursive call

# Example
print(gcd(52, 18))