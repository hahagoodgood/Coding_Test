import math


def is_prime(n: int) -> bool:
    """Check if n is a prime number."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:  
        return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True


N = int(input())
numbers = list(map(int, input().split()))

print(sum(1 for num in numbers if is_prime(num)))
