a = int(input())
result = a
cnt = 0
while 1 :
    sum = result//10 + result%10
    result = result%10*10 + sum%10
    cnt += 1
    if result == a: break
print(cnt)