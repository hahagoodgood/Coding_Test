a = int(input())
# [print(' '*i,'*'*(a-i)) for i in range(a)]
for i in range(a):
    str = ' '*i + '*'*(a-i)
    print(str)