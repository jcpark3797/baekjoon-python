# 약수 구하기
# 문제 번호: 2501번 (2)

target, key = map(int,input().split())
list_ = []
for i in range(1,target+1):
    if target%i == 0:
        list_.append(i)
if len(list_) < key: print(0)
else: print(list_[key-1])