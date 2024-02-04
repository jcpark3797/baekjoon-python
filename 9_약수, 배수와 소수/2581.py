# 소수
# 문제 번호: 2581번 (5)

param_start = int(input())
param_end = int(input())
list_result = []
for value in range(param_start, param_end+1):
    if len([i for i in range(2,int(value**0.5)+1) if value%i==0])==0 and value >= 2:
        list_result.append(value)
if list_result:
    print("{}\n{}".format(sum(list_result),min(list_result)))
else:
    print(-1)    