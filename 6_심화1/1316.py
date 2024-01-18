def solution(data):
    for i, k in enumerate(data):
        for j in range(i+1, len(data)):
            if (k!=data[j]):
                if(k in data[j:]):
                    return False
                else:
                    break
    return True

num = int(input())
cnt = 0
for _ in range(num):
    data = input()
    if solution(data):
        cnt += 1
print(cnt)