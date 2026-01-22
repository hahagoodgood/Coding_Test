# 입출력을 위한 모듈 sys
import sys

# S의 각 문자를 R만큼 반복하여 출력하는 함수
def repeated_print(R:int, S:str):
    # S의 각 문자를 순차적으로 접근
    for char in S:
        # char를 R만큼 반복하여 출력
        sys.stdout.write(char*R)
    # 줄바꿈
    sys.stdout.write('\n')

# 반복 출력을 몇 번 시행할 것인지 T 입력
T = int(sys.stdin.readline()) 

# T 만큼 반복 출력 작업 실행
for _ in range(T):
    # 반복 횟수 R과 문자열 S를 sys 모듈을 통해 입력받아 split()을 통해 공백 기준으로 분리
    R, S = sys.stdin.readline().split()
    # repeated_print 함수를 통해 R만큼 S를 반복 출력
    repeated_print(int(R), S)