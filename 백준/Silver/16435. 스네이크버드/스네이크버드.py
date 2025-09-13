import sys

#input the number of fruits(N), initial lenth(L)
N, L = map(int, sys.stdin.readline().split())
# H = list(map(int, sys.stdin.readline().split()))

#Eating fruit in order
for fruit in sorted(map(int, sys.stdin.readline().split()))[:N]:
    #If it can't eat break
    if L < fruit: break
    L+=1

sys.stdout.write(f"{L}")