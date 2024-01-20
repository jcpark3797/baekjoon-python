# 세탁소 사장 동혁
# 문제 번호: 2720번

dic = [0.25,0.10,0.05,0.01]
num = int(input())
for _ in range(num):
    data = float(input()) * 0.01
    result = []
    for k in dic:
        tmp = int(data/k)
        data = round(data - (k * tmp), 3)        
        result.append(str(tmp))
    print(*result)