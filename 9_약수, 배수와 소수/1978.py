# 소수 찾기
# 문제 번호: 1978번 (4)

num = int(input())
data = [int(x) for x in input().split() if int(x) >= 2]
count = 0
for value in data:
    if len([i for i in range(2, value) if value%i==0])==0:
        count += 1
print(count)