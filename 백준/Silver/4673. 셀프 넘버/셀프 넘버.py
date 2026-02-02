num_list = [0]*10001
for n in range(1, 10000):
    if num_list[n] == 0 : print(n)
    num = n + sum(int(i) for i in str(n))
    if num <= 10000 :
        num_list[num] = 1