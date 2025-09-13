# input the number of humen(N) and the time (h)
import sys

N = int(sys.stdin.readline())
#intput and sort the time
H = sorted(map(int, sys.stdin.readline().split()))
result = 0
for i in range(N):
    result += H.pop()*(i+1)
sys.stdout.write(f"{result}")