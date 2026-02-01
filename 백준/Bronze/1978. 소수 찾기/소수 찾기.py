import math

def is_prime(num:int):
    if num == 1 : return False
    elif num == 2 : return True
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0 : return False
    return True

N = int(input())
num_list = list(map(int,input().split()))
cnt_prm = 0
for num in num_list:
    if is_prime(num) : cnt_prm+=1
print(cnt_prm)
