N = int(input())
cnt = 1
while 1 :
    str_cnt = str(cnt)
    if N <= cnt :
        print(0)
        break
    if N == cnt + sum(map(int, str_cnt)) :
        print(cnt)
        break
    cnt += 1