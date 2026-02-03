N = int(input())
result = 0
for a in range(2, 10):
    for b in range(1, 10):
        if N == a or N == b or N == a*b:
            result = 1
            break
    if result :
        break

print(result)