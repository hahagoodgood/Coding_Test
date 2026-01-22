# sys module for input and output
import sys

# Factorial calculation function implemented recursively (return type: int)
def factorial(N:int):
    # Return 1 when N=0 to terminate recursion
    if N == 0 :
        return 1
    # Recursively calculate N*(N-1)! when N!=0
    else: return N*factorial(N-1)

# Input N to calculate factorial
N = int(sys.stdin.readline())
# Output the value calculated by the factorial function
sys.stdout.write(str(factorial(N)))