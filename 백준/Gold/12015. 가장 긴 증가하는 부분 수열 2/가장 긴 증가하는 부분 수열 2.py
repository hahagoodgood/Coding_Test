import sys
import bisect

def longest_increasing_subsequence_length(sequence):
    LIS = []
    for num in sequence:
        idx = bisect.bisect_left(LIS, num)
        if idx == len(LIS):
            LIS.append(num)
        else:
            LIS[idx] = num
    return len(LIS)

N = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
print(longest_increasing_subsequence_length(sequence))
