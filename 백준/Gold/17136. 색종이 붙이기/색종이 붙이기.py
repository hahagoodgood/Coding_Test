def is_valid(x, y, size, paper):
    # 색종이가 종이를 벗어나거나 이미 사용한 색종이라면 유효하지 않음
    if x + size > 10 or y + size > 10 or used_paper[size] == 5:
        return False
    else:
        # 색종이가 덮인 부분에 다른 색종이가 이미 있으면 유효하지 않음
        for i in range(x, x + size):
            for j in range(y, y + size):
                if paper[i][j] == 0 or visited[i][j]:
                    #paper가 0인 경우는 색종이의 범위를 벗어남
                    #visited가 1인 경우는 해당 영역이 이미 붙혀져 있다.
                    return False
    return True

def cover(x, y, size, value):
    # 색종이로 덮은 부분을 표시하고 색종이 사용 개수를 증가시킴
    for i in range(x, x + size):
        for j in range(y, y + size):
            visited[i][j] = value

def find_next():
    # 다음 덮어야 할 위치 찾기
    for i in range(10):
        for j in range(10):
            if paper[i][j] == 1 and not visited[i][j]:
                return (i, j)
    return (-1, -1)

def dfs(cnt):
    global answer

    # 현재까지 사용한 색종이의 개수가 answer보다 크다면 중단
    if cnt >= answer:
        return

    x, y = find_next()

    # 모든 부분이 덮혔다면 answer 갱신
    if x == -1 and y == -1:
        answer = min(answer, cnt)
        return
    else :
        # 색종이를 붙일 수 있는 가장 큰 크기부터 시작
        for size in range(5, 0, -1):
            if is_valid(x, y, size, paper):
                cover(x, y, size, 1)
                used_paper[size] += 1
                dfs(cnt + 1)
                used_paper[size] -= 1
                cover(x, y, size, 0)
2
# 입력
paper = [list(map(int, input().split())) for _ in range(10)]
visited = [[0] * 10 for _ in range(10)] #색종이를 붙였다는 것을 알려주기 위한 2차원 배열
used_paper = [0] * 6  # 각 크기의 색종이 사용 개수
answer = float('inf') #무한대를 의미한다. 

# 탐색 시작
dfs(0)

# 정답 출력
if answer == float('inf'):
    print(-1)
else:
    print(answer)



