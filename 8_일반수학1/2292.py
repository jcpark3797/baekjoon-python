# 벌집
# 문제 번호: 2292번 (5)

data = int(input())
if data == 1:
    print(1)
else:
    cnt = 2
    while True:
        if 3*(cnt-1)*(cnt-2)+2 <= data <= 3*cnt*(cnt-1)+1:
            break    
        cnt += 1
    print(cnt)