word = input()
result ="{"
for i in range(1,len(word)-1):
    for j in range(i+1, len(word)):
        front = word[:i][::-1]
        mid = word[i:j][::-1]
        end = word[j:][::-1]
        result = min(result, front+mid+end)

print(result)