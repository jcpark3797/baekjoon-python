# 소인수분해
# 문제 번호: 11653번 (6)

data = int(input())
my_point = 2
while data>1:    
    while data%my_point==0:
        data = data//my_point
        print(my_point)
    my_point += 1    