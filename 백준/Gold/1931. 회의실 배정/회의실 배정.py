# 입력
n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

# 회의를 종료 시간 기준으로 정렬, 종료 시간이 같으면 시작 시간 기준으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

# 그리디 알고리즘 적용
count = 0
end_time = 0

for start, end in meetings:
    if start >= end_time:
        end_time = end
        count += 1

# 결과 출력
print(count)