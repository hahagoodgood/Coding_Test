a = [] #톱니 리스트
scds = [] # 회전 리스트

##############################################################

def turn(x : list, drt):
    temp = 0
    if drt < 0 :
        temp = x[0]
        for i in range(len(x)-1):
            x[i] = x[i+1]
        x[7] = temp
    else :
        temp = x[7]
        for i in range(len(x)-1):
            x[7-i] = x[7-i-1]
        x[0] = temp

################################################################3

# 입력 리스트
# 톱니 입력
for _ in range(4):
    x = list(input())
    a.append(x)

n = int(input())

#스케줄 입력
for i in range(n):
   scd = list(map(int, input().split()))
   scds.append(scd)


import copy
# 스케줄 실행
for scd in scds:
    ta = copy.deepcopy(a)
    turn(a[scd[0]-1], scd[1])

    drc = scd[1] * (-1) #방향
    #왼쪽 회전
    for i in range(scd[0]-2,-1,-1):
        if ta[i][2] != ta[i+1][6]:
            turn(a[i], drc)
            drc *= -1
        else:
            break


    drc = scd[1] * (-1)
    # 오른쪽 회전
    for i in range(scd[0],4):
        if ta[i-1][2] != ta[i][6]:
            turn(a[i], drc)
            drc *= -1
        else:
            break
score = 0

for idx, whl in enumerate(a):
    if whl[0] == '1':
        score += 2**idx

print(score)