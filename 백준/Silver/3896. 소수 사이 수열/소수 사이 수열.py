import sys
import bisect

MAX = 1299709

is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX + 1, i):
            is_prime[j] = False

primes = [i for i, val in enumerate(is_prime) if val]

T = int(sys.stdin.readline())
for _ in range(T):
    k = int(sys.stdin.readline())
    if is_prime[k]:
        print(0)
    else:
        idx = bisect.bisect_left(primes, k)
        next_prime = primes[idx]
        prev_prime = primes[idx - 1]
        print(next_prime - prev_prime)