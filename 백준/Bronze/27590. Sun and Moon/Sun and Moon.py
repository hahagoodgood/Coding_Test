import math
d_s, y_s = map(int,input().split())
d_m, y_m = map(int,input().split())

step, result = (y_s, y_s-d_s) if y_s >= y_m else (y_m, y_m-d_m)
while (d_s+result)%y_s != 0 or (d_m+result)%y_m != 0 :
    result += step
print(result)