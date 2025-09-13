cnt = int(input())
lvl = sum  = 1
# for i in range(INT32_MAX):
#     sum += i
#     if sum >= cnt:
#         lvl = i
#         break
while lvl < 2*cnt/lvl-1:
    lvl += 1

n = cnt-(lvl-1)*lvl//2
if lvl%2 == 0:
    print(str(n)+'/'+str(lvl-n+1))
else:
    print(str(lvl-n+1) + '/' + str(n))