import math

N = int(input())
result = math.factorial(N)
cnt = 0

while result % 10 == 0 :
    result //= 10
    cnt += 1

print(cnt)