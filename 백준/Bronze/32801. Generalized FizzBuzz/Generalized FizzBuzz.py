n, a, b = map(int,input().split())
Fizz_cnt, Buzz_cnt, FizzBuzz_cnt = 0, 0, 0

for i in range(1,n+1):
    if (i % a == 0) and (i % b == 0) :
        FizzBuzz_cnt += 1
    elif i % a == 0 :
        Fizz_cnt += 1
    elif i % b == 0 :
        Buzz_cnt += 1

print(str(Fizz_cnt) + " " + str(Buzz_cnt) + " " + str(FizzBuzz_cnt))
