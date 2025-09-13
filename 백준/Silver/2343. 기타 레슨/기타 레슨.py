def minimum_bluray_size(lecture_lengths, M):
    left = max(lecture_lengths)  
    right = sum(lecture_lengths)  
    result = right

    while left <= right:
        mid = (left + right) // 2  
        count = 1  
        total = 0  

        for length in lecture_lengths:
            if total + length > mid:
                count += 1  
                total = 0
            total += length

        if count <= M:
            result = mid 
            right = mid - 1 
        else:
            left = mid + 1 

    return result

N, M = map(int, input().split())
lecture_lengths = list(map(int, input().split()))
print(minimum_bluray_size(lecture_lengths, M))
