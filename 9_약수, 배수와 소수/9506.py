# 약수들의 합
# 문제 번호: 9506번 (3)

while True:
    data = int(input())
    if data == -1: break
    list_ = [i for i in range(1, data) if data%i==0]
    if sum(list_)==data:
        print(data,"="," + ".join(list(map(str, list_))))
    else:
        print(data,"is NOT perfect.")