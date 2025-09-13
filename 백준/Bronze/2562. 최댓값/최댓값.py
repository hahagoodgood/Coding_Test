a = []
for i in range(9): a.append(int(input()))

Max = max(a)
index = a.index(Max)
print(Max)
print(index+1)
