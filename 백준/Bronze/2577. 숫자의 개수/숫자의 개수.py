def b2577(A:int, B:int, C:int):
    num = [0]*10
    for i in str(A*B*C): num[int(i)] += 1
    for i in num: print(i)

if __name__ == '__main__':
    n = []*3
    for _ in range(3): n.append(int(input()))
    b2577(*n)